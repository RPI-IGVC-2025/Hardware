#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped
from nav2_msgs.action import NavigateToPose
from robot_localization.srv import FromLL


class SingleGpsGoalNode(Node):
    def __init__(self):
        super().__init__("single_gps_goal_node")

        self.declare_parameter("latitude", 0.0)
        self.declare_parameter("longitude", 0.0)
        self.declare_parameter("altitude", 0.0)
        self.declare_parameter("yaw", 0.0)

        self.declare_parameter("global_frame", "map")
        self.declare_parameter("fromll_service", "/fromLL")
        self.declare_parameter("nav_action", "navigate_to_pose")

        self.declare_parameter("require_enabled", True)
        self.declare_parameter("enabled_topic", "/enabled")

        self.enabled = False
        self.sent_goal = False

        if bool(self.get_parameter("require_enabled").value):
            self.enabled_sub = self.create_subscription(
                Bool,
                self.get_parameter("enabled_topic").value,
                self.enabled_callback,
                10,
            )
        else:
            self.enabled = True

        self.fromll_client = self.create_client(
            FromLL,
            self.get_parameter("fromll_service").value,
        )

        self.nav_client = ActionClient(
            self,
            NavigateToPose,
            self.get_parameter("nav_action").value,
        )

        self.timer = self.create_timer(1.0, self.try_send_goal)

        self.get_logger().info("single_gps_goal_node started")

    def enabled_callback(self, msg: Bool):
        self.enabled = bool(msg.data)

    def try_send_goal(self):
        if self.sent_goal:
            return

        if not self.enabled:
            self.get_logger().info("Waiting for /enabled == true")
            return

        if not self.fromll_client.wait_for_service(timeout_sec=0.1):
            self.get_logger().warn("Waiting for /fromLL service")
            return

        if not self.nav_client.wait_for_server(timeout_sec=0.1):
            self.get_logger().warn("Waiting for Nav2 navigate_to_pose action")
            return

        lat = float(self.get_parameter("latitude").value)
        lon = float(self.get_parameter("longitude").value)
        alt = float(self.get_parameter("altitude").value)

        if abs(lat) < 1e-9 and abs(lon) < 1e-9:
            self.get_logger().error("Latitude/longitude are still 0.0. Refusing to send goal.")
            self.sent_goal = True
            return

        req = FromLL.Request()
        req.ll_point.latitude = lat
        req.ll_point.longitude = lon
        req.ll_point.altitude = alt

        self.get_logger().info(f"Converting GPS goal: lat={lat}, lon={lon}")

        future = self.fromll_client.call_async(req)
        future.add_done_callback(self.fromll_done_callback)

        self.sent_goal = True

    def fromll_done_callback(self, future):
        try:
            result = future.result()
        except Exception as exc:
            self.get_logger().error(f"/fromLL call failed: {exc}")
            return

        x = result.map_point.x
        y = result.map_point.y
        z = result.map_point.z

        yaw = float(self.get_parameter("yaw").value)

        goal = PoseStamped()
        goal.header.stamp = self.get_clock().now().to_msg()
        goal.header.frame_id = self.get_parameter("global_frame").value
        goal.pose.position.x = x
        goal.pose.position.y = y
        goal.pose.position.z = z

        goal.pose.orientation.z = math.sin(yaw / 2.0)
        goal.pose.orientation.w = math.cos(yaw / 2.0)

        self.get_logger().info(
            f"Sending Nav2 goal in {goal.header.frame_id}: x={x:.2f}, y={y:.2f}, yaw={yaw:.2f}"
        )

        nav_goal = NavigateToPose.Goal()
        nav_goal.pose = goal

        send_future = self.nav_client.send_goal_async(nav_goal)
        send_future.add_done_callback(self.nav_goal_response_callback)

    def nav_goal_response_callback(self, future):
        try:
            goal_handle = future.result()
        except Exception as exc:
            self.get_logger().error(f"Failed to send Nav2 goal: {exc}")
            return

        if not goal_handle.accepted:
            self.get_logger().error("Nav2 rejected GPS goal")
            return

        self.get_logger().info("Nav2 accepted GPS goal")


def main(args=None):
    rclpy.init(args=args)
    node = SingleGpsGoalNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()