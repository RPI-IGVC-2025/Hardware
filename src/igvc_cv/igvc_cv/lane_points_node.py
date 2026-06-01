#!/usr/bin/env python3

import math
from typing import Optional, Tuple

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from geometry_msgs.msg import PoseStamped
from message_filters import ApproximateTimeSynchronizer, Subscriber
from nav_msgs.msg import Path
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from sensor_msgs.msg import CameraInfo, Image, PointCloud2
from sensor_msgs_py import point_cloud2
from std_msgs.msg import Header


class LanePointsNode(Node):
    """
    Detect lane markings from RGB, use aligned depth to project them into 3D,
    and publish lane points for Nav2/local costmap and director debugging.

    Publishes:
      /lanes/points       PointCloud2 in camera optical frame
      /lanes/debug_image  Image showing detected Hough lines
      /left_boundary      Path in approximate base_link coordinates
      /right_boundary     Path in approximate base_link coordinates
    """

    def __init__(self):
        super().__init__("lane_points_node")
        self.bridge = CvBridge()
        self.camera_info: Optional[CameraInfo] = None

        # Topics
        self.declare_parameter("rgb_topic", "/zed/zed_node/rgb/image_rect_color")
        self.declare_parameter("depth_topic", "/zed/zed_node/depth/depth_registered")
        self.declare_parameter("camera_info_topic", "/zed/zed_node/rgb/camera_info")
        self.declare_parameter("points_topic", "/lanes/points")
        self.declare_parameter("debug_topic", "/lanes/debug_image")
        self.declare_parameter("left_path_topic", "/left_boundary")
        self.declare_parameter("right_path_topic", "/right_boundary")

        # Frames
        self.declare_parameter("lane_points_frame", "")  # blank = use depth image frame
        self.declare_parameter("path_frame", "base_link")

        # ROI
        self.declare_parameter("roi_top_fraction", 0.30)
        self.declare_parameter("roi_bottom_fraction", 0.88)

        # White mask, HLS
        self.declare_parameter("min_lightness", 120)
        self.declare_parameter("max_saturation", 190)

        # Blur / Canny / Hough
        self.declare_parameter("blur_kernel_size", 11)
        self.declare_parameter("blur_sigma_x", 33.0)
        self.declare_parameter("blur_sigma_y", 33.0)
        self.declare_parameter("canny_low", 10)
        self.declare_parameter("canny_high", 100)
        self.declare_parameter("hough_rho", 2.0)
        self.declare_parameter("hough_theta", math.pi / 180.0)
        self.declare_parameter("hough_threshold", 10)
        self.declare_parameter("hough_min_line_length", 4)
        self.declare_parameter("hough_max_line_gap", 5)
        self.declare_parameter("line_thickness", 10)

        # Geometry filters
        self.declare_parameter("min_depth_m", 0.3)
        self.declare_parameter("max_depth_m", 5.0)
        self.declare_parameter("max_abs_x_m", 4.0)  # camera optical x, left/right
        self.declare_parameter("max_points", 6000)
        self.declare_parameter("pixel_stride", 2)

        # Debug
        self.declare_parameter("log_counts", True)

        qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10,
        )

        self.rgb_sub = Subscriber(
            self, Image, self.get_parameter("rgb_topic").value, qos_profile=qos
        )
        self.depth_sub = Subscriber(
            self, Image, self.get_parameter("depth_topic").value, qos_profile=qos
        )

        self.info_sub = self.create_subscription(
            CameraInfo,
            self.get_parameter("camera_info_topic").value,
            self.info_callback,
            qos,
        )

        self.sync = ApproximateTimeSynchronizer(
            [self.rgb_sub, self.depth_sub],
            queue_size=10,
            slop=0.08,
        )
        self.sync.registerCallback(self.process)

        self.points_pub = self.create_publisher(
            PointCloud2, self.get_parameter("points_topic").value, 10
        )
        self.debug_pub = self.create_publisher(
            Image, self.get_parameter("debug_topic").value, 10
        )
        self.left_pub = self.create_publisher(
            Path, self.get_parameter("left_path_topic").value, 10
        )
        self.right_pub = self.create_publisher(
            Path, self.get_parameter("right_path_topic").value, 10
        )

        self.get_logger().info("lane_points_node started")

    def info_callback(self, msg: CameraInfo):
        self.camera_info = msg

    def process(self, rgb_msg: Image, depth_msg: Image):
        if self.camera_info is None:
            self.get_logger().warn("No CameraInfo received yet")
            return

        try:
            frame = self.bridge.imgmsg_to_cv2(rgb_msg, "bgr8")
            depth = self.bridge.imgmsg_to_cv2(depth_msg, desired_encoding="passthrough")
        except Exception as exc:
            self.get_logger().warn(f"Image conversion failed: {exc}")
            return

        depth = self.normalize_depth(depth)
        h, w = frame.shape[:2]

        line_mask, debug = self.detect_lane_mask(frame)

        points_camera = self.project_mask_to_3d(line_mask, depth, w, h)

        frame_id = self.get_parameter("lane_points_frame").value
        if not frame_id:
            frame_id = depth_msg.header.frame_id

        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = frame_id

        cloud = point_cloud2.create_cloud_xyz32(header, points_camera.tolist())
        self.points_pub.publish(cloud)

        left_path, right_path = self.make_boundary_paths(points_camera)
        self.left_pub.publish(left_path)
        self.right_pub.publish(right_path)

        debug_msg = self.bridge.cv2_to_imgmsg(debug, encoding="bgr8")
        debug_msg.header = rgb_msg.header
        self.debug_pub.publish(debug_msg)

        if bool(self.get_parameter("log_counts").value):
            self.get_logger().info(
                f"lane points={len(points_camera)}, "
                f"left={len(left_path.poses)}, right={len(right_path.poses)}"
            )

    def normalize_depth(self, depth: np.ndarray) -> np.ndarray:
        if depth.dtype == np.uint16:
            return depth.astype(np.float32) / 1000.0
        return depth.astype(np.float32)

    def detect_lane_mask(self, frame: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        h, w = frame.shape[:2]

        roi_top = int(h * float(self.get_parameter("roi_top_fraction").value))
        roi_bottom = int(h * float(self.get_parameter("roi_bottom_fraction").value))

        min_l = int(self.get_parameter("min_lightness").value)
        max_s = int(self.get_parameter("max_saturation").value)

        # White-ish lane mask in HLS
        hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
        lightness = hls[:, :, 1]
        saturation = hls[:, :, 2]

        white_mask = np.zeros((h, w), dtype=np.uint8)
        white_mask[(lightness >= min_l) & (saturation <= max_s)] = 255
        white_mask[:roi_top, :] = 0
        white_mask[roi_bottom:, :] = 0

        # Old tuned style: grayscale blur + Canny, but restricted by white mask
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_and(gray, gray, mask=white_mask)

        blur_k = int(self.get_parameter("blur_kernel_size").value)
        if blur_k % 2 == 0:
            blur_k += 1

        blur = cv2.GaussianBlur(
            gray,
            (blur_k, blur_k),
            float(self.get_parameter("blur_sigma_x").value),
            float(self.get_parameter("blur_sigma_y").value),
        )

        edges = cv2.Canny(
            blur,
            int(self.get_parameter("canny_low").value),
            int(self.get_parameter("canny_high").value),
        )

        lines = cv2.HoughLinesP(
            edges,
            float(self.get_parameter("hough_rho").value),
            float(self.get_parameter("hough_theta").value),
            int(self.get_parameter("hough_threshold").value),
            minLineLength=int(self.get_parameter("hough_min_line_length").value),
            maxLineGap=int(self.get_parameter("hough_max_line_gap").value),
        )

        line_mask = np.zeros((h, w), dtype=np.uint8)
        debug = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        thickness = int(self.get_parameter("line_thickness").value)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)

                # Keep only lines whose midpoint is within the ROI.
                mid_y = 0.5 * (y1 + y2)
                if mid_y < roi_top or mid_y > roi_bottom:
                    continue

                cv2.line(debug, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.line(line_mask, (x1, y1), (x2, y2), 255, thickness)

        # Keep only line-mask pixels that are still on white-ish pixels.
        line_mask = cv2.bitwise_and(line_mask, white_mask)

        return line_mask, debug

    def project_mask_to_3d(
        self,
        mask: np.ndarray,
        depth: np.ndarray,
        rgb_w: int,
        rgb_h: int,
    ) -> np.ndarray:
        fx = float(self.camera_info.k[0])
        fy = float(self.camera_info.k[4])
        cx = float(self.camera_info.k[2])
        cy = float(self.camera_info.k[5])

        min_d = float(self.get_parameter("min_depth_m").value)
        max_d = float(self.get_parameter("max_depth_m").value)
        max_abs_x = float(self.get_parameter("max_abs_x_m").value)
        stride = max(1, int(self.get_parameter("pixel_stride").value))
        max_points = int(self.get_parameter("max_points").value)

        vs, us = np.where(mask > 0)
        if len(us) == 0:
            return np.empty((0, 3), dtype=np.float32)

        us = us[::stride]
        vs = vs[::stride]

        # Scale RGB pixel coordinates to depth image coordinates if needed.
        depth_h, depth_w = depth.shape[:2]
        du = np.clip((us * depth_w / float(rgb_w)).astype(np.int32), 0, depth_w - 1)
        dv = np.clip((vs * depth_h / float(rgb_h)).astype(np.int32), 0, depth_h - 1)

        z = depth[dv, du]

        valid = np.isfinite(z) & (z >= min_d) & (z <= max_d)
        us = us[valid].astype(np.float32)
        vs = vs[valid].astype(np.float32)
        z = z[valid].astype(np.float32)

        if len(z) == 0:
            return np.empty((0, 3), dtype=np.float32)

        x = (us - cx) * z / fx
        y = (vs - cy) * z / fy

        valid = np.isfinite(x) & np.isfinite(y) & (np.abs(x) <= max_abs_x)
        x = x[valid]
        y = y[valid]
        z = z[valid]

        points = np.vstack((x, y, z)).T.astype(np.float32)

        if len(points) > max_points:
            idx = np.linspace(0, len(points) - 1, max_points).astype(np.int32)
            points = points[idx]

        return points

    def make_boundary_paths(self, points_camera: np.ndarray) -> Tuple[Path, Path]:
        """
        Convert camera optical points into approximate base_link-style points.

        Camera optical convention:
          x = right
          y = down
          z = forward

        Approx base_link convention:
          x = forward = camera z
          y = left    = -camera x
          z = 0
        """
        stamp = self.get_clock().now().to_msg()
        frame_id = self.get_parameter("path_frame").value

        left_path = Path()
        right_path = Path()
        left_path.header.stamp = stamp
        right_path.header.stamp = stamp
        left_path.header.frame_id = frame_id
        right_path.header.frame_id = frame_id

        if len(points_camera) == 0:
            return left_path, right_path

        base_x = points_camera[:, 2]
        base_y = -points_camera[:, 0]

        base_points = np.vstack((base_x, base_y)).T
        base_points = base_points[base_points[:, 0].argsort()]

        for x, y in base_points:
            pose = PoseStamped()
            pose.header.stamp = stamp
            pose.header.frame_id = frame_id
            pose.pose.position.x = float(x)
            pose.pose.position.y = float(y)
            pose.pose.position.z = 0.0
            pose.pose.orientation.w = 1.0

            if y >= 0.0:
                left_path.poses.append(pose)
            else:
                right_path.poses.append(pose)

        return left_path, right_path


def main(args=None):
    rclpy.init(args=args)
    node = LanePointsNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()