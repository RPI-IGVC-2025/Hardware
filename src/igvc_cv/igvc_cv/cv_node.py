import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, PointCloud2
from cv_bridge import CvBridge
from message_filters import ApproximateTimeSynchronizer, Subscriber
import sensor_msgs_py.point_cloud2 as pc2
import cv2
import numpy as np


class CVNode(Node):
    def __init__(self):
        super().__init__('cv_node')
        self.bridge = CvBridge()

        # Gaussian blur
        self.declare_parameter("blur_kernel_size", 11)
        self.declare_parameter("blur_sigma_x", 33.0)
        self.declare_parameter("blur_sigma_y", 33.0)

        # Canny edge detection
        self.declare_parameter("canny_low", 10)
        self.declare_parameter("canny_high", 100)

        # Hough Line Transform
        self.declare_parameter("hough_rho", 2.0)
        self.declare_parameter("hough_theta", np.pi / 180)
        self.declare_parameter("hough_threshold", 10)
        self.declare_parameter("hough_min_line_length", 4)
        self.declare_parameter("hough_max_line_gap", 5)

        self.declare_parameter("line_thickness", 10)

        # Synchronised RGB + PointCloud subscribers
        self.rgb_sub = Subscriber(self, Image, 'image_raw')
        self.pc_sub = Subscriber(self, PointCloud2, 'depth/points')
        self.sync = ApproximateTimeSynchronizer(
            [self.rgb_sub, self.pc_sub],
            queue_size=10,
            slop=0.05
        )
        self.sync.registerCallback(self.process)
        # ===== Publishers =====
        self.image_pub = self.create_publisher(Image, 'image_processed', 10)

    # ── Main callback ─────────────────────────────────────────────────────
    def process(self, rgb_msg: Image, pc_msg: PointCloud2):

        # Fetch parameters
        blur_k = self.get_parameter("blur_kernel_size").value
        blur_sx = self.get_parameter("blur_sigma_x").value
        blur_sy = self.get_parameter("blur_sigma_y").value
        canny_low = self.get_parameter("canny_low").value
        canny_high = self.get_parameter("canny_high").value
        hough_rho = self.get_parameter("hough_rho").value
        hough_theta = self.get_parameter("hough_theta").value
        hough_thresh = self.get_parameter("hough_threshold").value
        hough_min_len = self.get_parameter("hough_min_line_length").value
        hough_max_gap = self.get_parameter("hough_max_line_gap").value
        thickness = self.get_parameter("line_thickness").value

        # Convert ROS image to OpenCV
        frame = self.bridge.imgmsg_to_cv2(rgb_msg, 'bgr8')
        h, w  = frame.shape[:2]

        # Convert to grayscale
        gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Gaussian Blur
        blur  = cv2.GaussianBlur(gray, (blur_k, blur_k), blur_sx, blur_sy)
        
        # Canny edge detection
        edges = cv2.Canny(blur, canny_low, canny_high)

        # Hough Line Transform
        lines = cv2.HoughLinesP(
            edges,
            hough_rho, hough_theta, hough_thresh,
            minLineLength=hough_min_len,
            maxLineGap=hough_max_gap
        )

        # Mask of detected line segments
        line_mask  = np.zeros((h, w), dtype=np.uint8)
        line_image = np.zeros_like(frame)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 255), thickness)
                cv2.line(line_mask, (x1, y1), (x2, y2), 255, thickness)

        # Read 3D points directly from point cloud 
        white_v, white_u = np.where(line_mask > 0)

        # Read the full cloud
        cloud_array = pc2.read_points_numpy(
            pc_msg,
            field_names=("x", "y", "z"),
            skip_nans=False,
            reshape_organized_cloud=True # shape (HxWx3)
        )
        
        # Look up 3D coords for each white pixel directly
        white_points = cloud_array[white_v, white_u] # Nx3

        # No depth return)
        valid = np.isfinite(white_points).all(axis=1)
        white_points = white_points[valid]

        # Publish image 
        result = cv2.addWeighted(frame, 0.8, line_image, 1.0, 1)
        ros_image = self.bridge.cv2_to_imgmsg(result, 'bgr8')
        ros_image.header = rgb_msg.header
        self.image_pub.publish(ros_image)
        
def main(args=None):
    rclpy.init(args=args)
    node = CVNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()