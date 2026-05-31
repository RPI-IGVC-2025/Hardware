#!/usr/bin/env python3

import math
from typing import List, Tuple

import cv2
import numpy as np
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image, PointCloud2
from sensor_msgs_py import point_cloud2
from std_msgs.msg import Header

from message_filters import Subscriber, ApproximateTimeSynchronizer


class LanePointsNode(Node):
    """
    Detect lane markings in the ZED RGB image, sample matching pixels from the
    registered ZED pointcloud, and publish those 3D lane points as PointCloud2.

    Output is intended to be consumed by Nav2's local voxel_layer as a marking
    source, so lanes become costmap obstacles.
    """

    def __init__(self):
        super().__init__("lane_points_node")

        # Topics
        self.declare_parameter("image_topic", "/zed/zed_node/rgb/image_rect_color")
        self.declare_parameter("cloud_topic", "/zed/zed_node/point_cloud/cloud_registered")
        self.declare_parameter("output_topic", "/lanes/points")

        # Image filtering
        self.declare_parameter("roi_top_fraction", 0.45)      # ignore top 45% of image
        self.declare_parameter("min_value", 170)              # HSV V threshold
        self.declare_parameter("max_saturation", 90)          # HSV S threshold
        self.declare_parameter("morph_kernel_size", 5)
        self.declare_parameter("min_component_area_px", 80)

        # Sampling and geometry filtering
        self.declare_parameter("pixel_stride", 4)             # sample every Nth lane pixel
        self.declare_parameter("max_points", 3000)
        self.declare_parameter("min_depth_m", 0.4)            # camera optical z
        self.declare_parameter("max_depth_m", 8.0)
        self.declare_parameter("max_abs_x_m", 5.0)            # camera optical x left/right
        self.declare_parameter("max_abs_y_m", 2.5)            # camera optical y up/down

        # Debug
        self.declare_parameter("publish_debug_image", True)
        self.declare_parameter("debug_image_topic", "/lanes/debug_mask")

        self.bridge = CvBridge()

        self.image_topic = self.get_parameter("image_topic").value
        self.cloud_topic = self.get_parameter("cloud_topic").value
        self.output_topic = self.get_parameter("output_topic").value

        self.pub_points = self.create_publisher(PointCloud2, self.output_topic, 10)

        self.publish_debug_image = bool(self.get_parameter("publish_debug_image").value)
        if self.publish_debug_image:
            self.pub_debug = self.create_publisher(
                Image,
                self.get_parameter("debug_image_topic").value,
                10,
            )
        else:
            self.pub_debug = None

        self.image_sub = Subscriber(self, Image, self.image_topic)
        self.cloud_sub = Subscriber(self, PointCloud2, self.cloud_topic)

        self.sync = ApproximateTimeSynchronizer(
            [self.image_sub, self.cloud_sub],
            queue_size=10,
            slop=0.08,
        )
        self.sync.registerCallback(self.callback)

        self.get_logger().info(
            f"LanePointsNode listening to image={self.image_topic}, "
            f"cloud={self.cloud_topic}, publishing {self.output_topic}"
        )

    def callback(self, image_msg: Image, cloud_msg: PointCloud2):
        try:
            bgr = self.bridge.imgmsg_to_cv2(image_msg, desired_encoding="bgr8")
        except Exception as exc:
            self.get_logger().warn(f"Could not convert image: {exc}")
            return

        height, width = bgr.shape[:2]

        if cloud_msg.height <= 1:
            self.get_logger().warn(
                "Input pointcloud is not organized. Need an organized registered ZED cloud."
            )
            return

        if cloud_msg.width != width or cloud_msg.height != height:
            self.get_logger().warn(
                f"Image/cloud size mismatch: image={width}x{height}, "
                f"cloud={cloud_msg.width}x{cloud_msg.height}. "
                "UV association may be wrong."
            )
            return

        mask = self.make_lane_mask(bgr)

        uv_samples = self.mask_to_uv_samples(mask)
        if not uv_samples:
            self.publish_empty_cloud(cloud_msg.header)
            return

        points = self.sample_cloud_points(cloud_msg, uv_samples)

        out_msg = point_cloud2.create_cloud_xyz32(cloud_msg.header, points)
        self.pub_points.publish(out_msg)

        if self.pub_debug is not None:
            debug_msg = self.bridge.cv2_to_imgmsg(mask, encoding="mono8")
            debug_msg.header = image_msg.header
            self.pub_debug.publish(debug_msg)

    def make_lane_mask(self, bgr: np.ndarray) -> np.ndarray:
        height, width = bgr.shape[:2]

        roi_top_fraction = float(self.get_parameter("roi_top_fraction").value)
        min_value = int(self.get_parameter("min_value").value)
        max_saturation = int(self.get_parameter("max_saturation").value)
        kernel_size = int(self.get_parameter("morph_kernel_size").value)
        min_area = int(self.get_parameter("min_component_area_px").value)

        hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)

        # White-ish lane marking: high brightness, low saturation.
        lower = np.array([0, 0, min_value], dtype=np.uint8)
        upper = np.array([180, max_saturation, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)

        # Ignore upper part of image.
        roi_start = int(height * roi_top_fraction)
        mask[:roi_start, :] = 0

        # Clean small holes/noise.
        kernel_size = max(3, kernel_size)
        if kernel_size % 2 == 0:
            kernel_size += 1

        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # Remove tiny connected components.
        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
        cleaned = np.zeros_like(mask)

        for label in range(1, num_labels):
            area = stats[label, cv2.CC_STAT_AREA]
            if area >= min_area:
                cleaned[labels == label] = 255

        return cleaned

    def mask_to_uv_samples(self, mask: np.ndarray) -> List[Tuple[int, int]]:
        stride = int(self.get_parameter("pixel_stride").value)
        max_points = int(self.get_parameter("max_points").value)

        ys, xs = np.where(mask > 0)

        if len(xs) == 0:
            return []

        # Stride first to reduce pointcloud lookup cost.
        xs = xs[::stride]
        ys = ys[::stride]

        # Cap total points.
        if len(xs) > max_points:
            idx = np.linspace(0, len(xs) - 1, max_points).astype(np.int32)
            xs = xs[idx]
            ys = ys[idx]

        return [(int(u), int(v)) for u, v in zip(xs, ys)]

    def sample_cloud_points(
        self,
        cloud_msg: PointCloud2,
        uv_samples: List[Tuple[int, int]],
    ) -> List[Tuple[float, float, float]]:
        min_depth = float(self.get_parameter("min_depth_m").value)
        max_depth = float(self.get_parameter("max_depth_m").value)
        max_abs_x = float(self.get_parameter("max_abs_x_m").value)
        max_abs_y = float(self.get_parameter("max_abs_y_m").value)

        points_out: List[Tuple[float, float, float]] = []

        # ZED registered cloud in camera optical frame is typically:
        # x = right, y = down, z = forward.
        # We keep the original cloud frame. Nav2/TF can transform it.
        for p in point_cloud2.read_points(
            cloud_msg,
            field_names=("x", "y", "z"),
            skip_nans=True,
            uvs=uv_samples,
        ):
            x = float(p[0])
            y = float(p[1])
            z = float(p[2])

            if not (math.isfinite(x) and math.isfinite(y) and math.isfinite(z)):
                continue

            # In camera optical frame, z is forward range/depth.
            if z < min_depth or z > max_depth:
                continue
            if abs(x) > max_abs_x:
                continue
            if abs(y) > max_abs_y:
                continue

            points_out.append((x, y, z))

        return points_out

    def publish_empty_cloud(self, header: Header):
        self.pub_points.publish(point_cloud2.create_cloud_xyz32(header, []))


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