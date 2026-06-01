#!/usr/bin/env python3

import math
from typing import Optional, Tuple

import numpy as np
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from geometry_msgs.msg import PointStamped, PoseStamped
from nav2_msgs.action import NavigateToPose
from sensor_msgs.msg import PointCloud2
from sensor_msgs_py import point_cloud2
from std_msgs.msg import Bool

import tf2_ros
from tf2_geometry_msgs import do_transform_point


class LaneDirectorNode(Node):
    """
    Director node for lane following.

    Subscribes:
      /enabled      std_msgs/Bool
      /lanes/points sensor_msgs/PointCloud2

    Sends:
      NavigateToPose goals to Nav2

    Core idea:
      - Transform lane points into base_link.
      - Use points in front of robot.
      - Split points into left and right lane groups by y position.
      - Fit simple y = m*x + b lines.
      - Pick a centered goal ahead of the robot.
      - Transform that goal into map frame.
      - Send it to Nav2.
    """

    def __init__(self):
        super().__init__("lane_director_node")

        # Topics / frames
        self.declare_parameter("enabled_topic", "/enabled")
        self.declare_parameter("lane_points_topic", "/lanes/points")
        self.declare_parameter("base_frame", "base_link")
        self.declare_parameter("global_frame", "map")

        # Lane following behavior
        self.declare_parameter("goal_period_s", 1.0)
        self.declare_parameter("lookahead_distance_m", 3.0)
        self.declare_parameter("min_x_m", 0.5)
        self.declare_parameter("max_x_m", 6.0)
        self.declare_parameter("max_abs_y_m", 3.0)
        self.declare_parameter("side_split_y_m", 0.15)

        # Lane geometry fallback
        self.declare_parameter("nominal_lane_width_m", 1.2)
        self.declare_parameter("max_center_y_m", 1.0)

        # Robustness
        self.declare_parameter("min_points_per_side", 8)
        self.declare_parameter("min_total_points", 12)
        self.declare_parameter("goal_update_min_distance_m", 0.35)

        self.enabled = False
        self.latest_cloud: Optional[PointCloud2] = None
        self.last_goal_xy_map: Optional[Tuple[float, float]] = None

        self.enabled_sub = self.create_subscription(
            Bool,
            self.get_parameter("enabled_topic").value,
            self.enabled_callback,
            10,
        )

        self.lane_sub = self.create_subscription(
            PointCloud2,
            self.get_parameter("lane_points_topic").value,
            self.lane_points_callback,
            10,
        )

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        self.nav_client = ActionClient(self, NavigateToPose, "navigate_to_pose")

        self.timer = self.create_timer(
            float(self.get_parameter("goal_period_s").value),
            self.timer_callback,
        )

        self.get_logger().info("Lane director node started. Waiting for /enabled.")

    def enabled_callback(self, msg: Bool):
        self.enabled = bool(msg.data)

    def lane_points_callback(self, msg: PointCloud2):
        self.latest_cloud = msg

    def timer_callback(self):
        if not self.enabled:
            return

        if self.latest_cloud is None:
            self.get_logger().warn("No /lanes/points received yet.")
            return

        if not self.nav_client.wait_for_server(timeout_sec=0.1):
            self.get_logger().warn("Nav2 navigate_to_pose action not available.")
            return

        points_base = self.cloud_to_base_points(self.latest_cloud)
        if points_base is None or len(points_base) == 0:
            self.get_logger().warn("No usable lane points after TF/filtering.")
            return

        center_goal_base = self.compute_center_goal(points_base)
        if center_goal_base is None:
            self.get_logger().warn("Could not compute lane center goal.")
            return

        goal_map = self.base_goal_to_map_pose(center_goal_base)
        if goal_map is None:
            self.get_logger().warn("Could not transform lane goal to map.")
            return

        if not self.should_send_goal(goal_map):
            return

        self.send_nav_goal(goal_map)

    def cloud_to_base_points(self, cloud_msg: PointCloud2) -> Optional[np.ndarray]:
        """
        Convert input PointCloud2 into Nx3 array in base_link frame.
        """
        base_frame = self.get_parameter("base_frame").value

        try:
            transform = self.tf_buffer.lookup_transform(
                base_frame,
                cloud_msg.header.frame_id,
                rclpy.time.Time(),
                timeout=rclpy.duration.Duration(seconds=0.1),
            )
        except Exception as exc:
            self.get_logger().warn(
                f"Could not lookup TF {base_frame} <- {cloud_msg.header.frame_id}: {exc}",
            )
            return None

        raw_points = []
        for p in point_cloud2.read_points(
            cloud_msg,
            field_names=("x", "y", "z"),
            skip_nans=True,
        ):
            x = float(p[0])
            y = float(p[1])
            z = float(p[2])

            if not (math.isfinite(x) and math.isfinite(y) and math.isfinite(z)):
                continue

            ps = PointStamped()
            ps.header = cloud_msg.header
            ps.point.x = x
            ps.point.y = y
            ps.point.z = z

            try:
                pt_base = do_transform_point(ps, transform)
            except Exception:
                continue

            raw_points.append([
                pt_base.point.x,
                pt_base.point.y,
                pt_base.point.z,
            ])

        if not raw_points:
            return None

        points = np.array(raw_points, dtype=np.float32)

        min_x = float(self.get_parameter("min_x_m").value)
        max_x = float(self.get_parameter("max_x_m").value)
        max_abs_y = float(self.get_parameter("max_abs_y_m").value)

        # base_link convention:
        # x forward, y left, z up
        mask = (
            (points[:, 0] >= min_x) &
            (points[:, 0] <= max_x) &
            (np.abs(points[:, 1]) <= max_abs_y)
        )

        return points[mask]

    def compute_center_goal(self, points_base: np.ndarray) -> Optional[Tuple[float, float]]:
        """
        Returns a goal point in base_link frame: (x_goal, y_goal).
        """
        min_total = int(self.get_parameter("min_total_points").value)
        if len(points_base) < min_total:
            return None

        lookahead = float(self.get_parameter("lookahead_distance_m").value)
        side_split = float(self.get_parameter("side_split_y_m").value)
        nominal_width = float(self.get_parameter("nominal_lane_width_m").value)
        max_center_y = float(self.get_parameter("max_center_y_m").value)
        min_side_points = int(self.get_parameter("min_points_per_side").value)

        # Split lane points.
        left = points_base[points_base[:, 1] > side_split]
        right = points_base[points_base[:, 1] < -side_split]

        left_y = self.estimate_y_at_x(left, lookahead) if len(left) >= min_side_points else None
        right_y = self.estimate_y_at_x(right, lookahead) if len(right) >= min_side_points else None

        if left_y is not None and right_y is not None:
            center_y = 0.5 * (left_y + right_y)

        elif left_y is not None:
            # Only left lane visible. Drive nominally half a lane width to its right.
            center_y = left_y - nominal_width / 2.0

        elif right_y is not None:
            # Only right lane visible. Drive nominally half a lane width to its left.
            center_y = right_y + nominal_width / 2.0

        else:
            return None

        center_y = float(np.clip(center_y, -max_center_y, max_center_y))

        return lookahead, center_y

    def estimate_y_at_x(self, points: np.ndarray, x_query: float) -> Optional[float]:
        """
        Fit y = m*x + b and evaluate y at x_query.
        """
        if len(points) < 2:
            return None

        x = points[:, 0]
        y = points[:, 1]

        try:
            m, b = np.polyfit(x, y, deg=1)
        except Exception:
            return None

        y_query = m * x_query + b

        if not math.isfinite(y_query):
            return None

        return float(y_query)

    def base_goal_to_map_pose(self, goal_base_xy: Tuple[float, float]) -> Optional[PoseStamped]:
        """
        Transform a base_link-frame goal point into map frame and create PoseStamped.
        """
        base_frame = self.get_parameter("base_frame").value
        global_frame = self.get_parameter("global_frame").value

        x_base, y_base = goal_base_xy

        goal_base = PointStamped()
        goal_base.header.stamp = self.get_clock().now().to_msg()
        goal_base.header.frame_id = base_frame
        goal_base.point.x = x_base
        goal_base.point.y = y_base
        goal_base.point.z = 0.0

        try:
            transform = self.tf_buffer.lookup_transform(
                global_frame,
                base_frame,
                rclpy.time.Time(),
                timeout=rclpy.duration.Duration(seconds=0.1),
            )
            goal_map_point = do_transform_point(goal_base, transform)
        except Exception as exc:
            self.get_logger().warn(
                f"Could not transform goal {global_frame} <- {base_frame}: {exc}",
            )
            return None

        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.header.frame_id = global_frame
        pose.pose.position.x = goal_map_point.point.x
        pose.pose.position.y = goal_map_point.point.y
        pose.pose.position.z = 0.0

        # Face generally toward the selected goal in base frame.
        yaw_base = math.atan2(y_base, x_base)

        # Because this pose is in map frame, we need map-frame yaw.
        # Simple method: get current base yaw in map, then add yaw_base.
        yaw_map = self.get_current_base_yaw_in_map()
        if yaw_map is None:
            yaw_map = 0.0

        yaw = yaw_map + yaw_base
        qz = math.sin(yaw / 2.0)
        qw = math.cos(yaw / 2.0)

        pose.pose.orientation.z = qz
        pose.pose.orientation.w = qw

        return pose

    def get_current_base_yaw_in_map(self) -> Optional[float]:
        global_frame = self.get_parameter("global_frame").value
        base_frame = self.get_parameter("base_frame").value

        try:
            transform = self.tf_buffer.lookup_transform(
                global_frame,
                base_frame,
                rclpy.time.Time(),
                timeout=rclpy.duration.Duration(seconds=0.1),
            )
        except Exception:
            return None

        q = transform.transform.rotation
        # yaw from quaternion
        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        return math.atan2(siny_cosp, cosy_cosp)

    def should_send_goal(self, goal: PoseStamped) -> bool:
        """
        Avoid spamming Nav2 with nearly identical goals.
        """
        x = goal.pose.position.x
        y = goal.pose.position.y

        if self.last_goal_xy_map is None:
            self.last_goal_xy_map = (x, y)
            return True

        last_x, last_y = self.last_goal_xy_map
        dist = math.hypot(x - last_x, y - last_y)

        min_dist = float(self.get_parameter("goal_update_min_distance_m").value)

        if dist >= min_dist:
            self.last_goal_xy_map = (x, y)
            return True

        return False

    def send_nav_goal(self, pose: PoseStamped):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = pose

        self.get_logger().info(
            f"Sending lane goal: x={pose.pose.position.x:.2f}, "
            f"y={pose.pose.position.y:.2f}, frame={pose.header.frame_id}"
        )

        send_future = self.nav_client.send_goal_async(goal_msg)
        send_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        try:
            goal_handle = future.result()
        except Exception as exc:
            self.get_logger().warn(f"NavigateToPose goal send failed: {exc}")
            return

        if not goal_handle.accepted:
            self.get_logger().warn("NavigateToPose goal rejected.")
            return

        self.get_logger().debug("NavigateToPose goal accepted.")


def main(args=None):
    rclpy.init(args=args)
    node = LaneDirectorNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()