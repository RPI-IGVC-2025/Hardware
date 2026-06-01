#!/usr/bin/env python3

import math
import struct
from typing import List, Tuple

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from message_filters import ApproximateTimeSynchronizer, Subscriber
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy
from sensor_msgs.msg import Image, PointCloud2
from sensor_msgs_py import point_cloud2


class LanePointsNode(Node):
    def __init__(self):
        super().__init__("lane_points_node")

        self.declare_parameter("image_topic", "/zed/zed_node/rgb/image_rect_color")
        self.declare_parameter("cloud_topic", "/zed/zed_node/point_cloud/cloud_registered")
        self.declare_parameter("points_topic", "/lanes/points")
        self.declare_parameter("debug_topic", "/lanes/debug_image")

        # Image filtering
        self.declare_parameter("roi_top_fraction", 0.40)
        self.declare_parameter("min_lightness", 130)
        self.declare_parameter("max_saturation", 170)

        # Canny / Hough
        self.declare_parameter("canny_low", 50)
        self.declare_parameter("canny_high", 150)
        self.declare_parameter("hough_threshold", 25)
        self.declare_parameter("hough_min_line_length", 35)
        self.declare_parameter("hough_max_line_gap", 30)
        self.declare_parameter("line_sample_step_px", 5)

        # 3D filtering
        self.declare_parameter("min_range_m", 0.3)
        self.declare_parameter("max_range_m", 5.0)
        self.declare_parameter("max_abs_xyz_m", 20.0)
        self.declare_parameter("max_points", 3000)

        self.bridge = CvBridge()

        self.points_pub = self.create_publisher(
            PointCloud2,
            self.get_parameter("points_topic").value,
            10,
        )

        self.debug_pub = self.create_publisher(
            Image,
            self.get_parameter("debug_topic").value,
            10,
        )

        sensor_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.VOLATILE,
            history=HistoryPolicy.KEEP_LAST,
            depth=5,
        )

        self.image_sub = Subscriber(
            self,
            Image,
            self.get_parameter("image_topic").value,
            qos_profile=sensor_qos,
        )

        self.cloud_sub = Subscriber(
            self,
            PointCloud2,
            self.get_parameter("cloud_topic").value,
            qos_profile=sensor_qos,
        )

        self.sync = ApproximateTimeSynchronizer(
            [self.image_sub, self.cloud_sub],
            queue_size=20,
            slop=0.25,
        )
        self.sync.registerCallback(self.callback)

        self.get_logger().info("lane_points_node started")

    def callback(self, image_msg: Image, cloud_msg: PointCloud2):
        try:
            bgr = self.bridge.imgmsg_to_cv2(image_msg, desired_encoding="bgr8")
        except Exception as exc:
            self.get_logger().warn(f"Image conversion failed: {exc}")
            self.publish_points(cloud_msg.header, [])
            return

        if cloud_msg.height <= 1:
            self.get_logger().warn("PointCloud2 is not organized; cannot UV-index it")
            self.publish_points(cloud_msg.header, [])
            return

        image_h, image_w = bgr.shape[:2]

        line_uvs_image, debug_img = self.detect_lane_line_pixels(bgr)
        line_uvs_cloud = self.scale_uvs_to_cloud(
            line_uvs_image,
            image_w,
            image_h,
            cloud_msg.width,
            cloud_msg.height,
        )

        points = self.read_cloud_points(cloud_msg, line_uvs_cloud)
        self.publish_points(cloud_msg.header, points)

        debug_msg = self.bridge.cv2_to_imgmsg(debug_img, encoding="bgr8")
        debug_msg.header = image_msg.header
        self.debug_pub.publish(debug_msg)

        self.get_logger().info(
            f"lane debug: lines_uv={len(line_uvs_image)}, points={len(points)}"
        )

    def detect_lane_line_pixels(self, bgr: np.ndarray) -> Tuple[List[Tuple[int, int]], np.ndarray]:
        h, w = bgr.shape[:2]

        roi_top = int(h * float(self.get_parameter("roi_top_fraction").value))
        min_lightness = int(self.get_parameter("min_lightness").value)
        max_saturation = int(self.get_parameter("max_saturation").value)

        hls = cv2.cvtColor(bgr, cv2.COLOR_BGR2HLS)
        lightness = hls[:, :, 1]
        saturation = hls[:, :, 2]

        mask = np.zeros((h, w), dtype=np.uint8)
        mask[(lightness >= min_lightness) & (saturation <= max_saturation)] = 255
        mask[:roi_top, :] = 0

        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        edges = cv2.Canny(
            mask,
            int(self.get_parameter("canny_low").value),
            int(self.get_parameter("canny_high").value),
        )

        lines = cv2.HoughLinesP(
            edges,
            rho=1,
            theta=np.pi / 180.0,
            threshold=int(self.get_parameter("hough_threshold").value),
            minLineLength=int(self.get_parameter("hough_min_line_length").value),
            maxLineGap=int(self.get_parameter("hough_max_line_gap").value),
        )

        debug = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        if lines is None:
            return [], debug

        sample_step = max(1, int(self.get_parameter("line_sample_step_px").value))
        max_points = int(self.get_parameter("max_points").value)

        uvs: List[Tuple[int, int]] = []

        for line in lines:
            x1, y1, x2, y2 = line[0]
            length = math.hypot(x2 - x1, y2 - y1)
            samples = max(2, int(length / sample_step))

            cv2.line(debug, (x1, y1), (x2, y2), (0, 255, 0), 2)

            for i in range(samples):
                t = i / float(samples - 1)
                u = int(round((1.0 - t) * x1 + t * x2))
                v = int(round((1.0 - t) * y1 + t * y2))

                if 0 <= u < w and 0 <= v < h:
                    uvs.append((u, v))

        if len(uvs) > max_points:
            idx = np.linspace(0, len(uvs) - 1, max_points).astype(np.int32)
            uvs = [uvs[i] for i in idx]

        return uvs, debug

    def scale_uvs_to_cloud(
        self,
        image_uvs: List[Tuple[int, int]],
        image_w: int,
        image_h: int,
        cloud_w: int,
        cloud_h: int,
    ) -> List[Tuple[int, int]]:
        if image_w == cloud_w and image_h == cloud_h:
            return image_uvs

        sx = cloud_w / float(image_w)
        sy = cloud_h / float(image_h)

        cloud_uvs = []
        for u, v in image_uvs:
            cu = int(np.clip(u * sx, 0, cloud_w - 1))
            cv = int(np.clip(v * sy, 0, cloud_h - 1))
            cloud_uvs.append((cu, cv))

        return cloud_uvs

    def read_cloud_points(
        self,
        cloud_msg: PointCloud2,
        uvs: List[Tuple[int, int]],
    ) -> List[Tuple[float, float, float]]:
        fields = {f.name: f.offset for f in cloud_msg.fields}
        if not all(k in fields for k in ("x", "y", "z")):
            self.get_logger().warn("PointCloud2 missing x/y/z fields")
            return []

        min_range = float(self.get_parameter("min_range_m").value)
        max_range = float(self.get_parameter("max_range_m").value)
        max_abs = float(self.get_parameter("max_abs_xyz_m").value)

        points = []

        for u, v in uvs:
            offset = v * cloud_msg.row_step + u * cloud_msg.point_step

            try:
                x = struct.unpack_from("f", cloud_msg.data, offset + fields["x"])[0]
                y = struct.unpack_from("f", cloud_msg.data, offset + fields["y"])[0]
                z = struct.unpack_from("f", cloud_msg.data, offset + fields["z"])[0]
            except Exception:
                continue

            if not (math.isfinite(x) and math.isfinite(y) and math.isfinite(z)):
                continue

            r = math.sqrt(x * x + y * y + z * z)
            if r < min_range or r > max_range:
                continue

            if abs(x) > max_abs or abs(y) > max_abs or abs(z) > max_abs:
                continue

            points.append((x, y, z))

        return points

    def publish_points(self, header, points: List[Tuple[float, float, float]]):
        msg = point_cloud2.create_cloud_xyz32(header, points)
        self.points_pub.publish(msg)


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