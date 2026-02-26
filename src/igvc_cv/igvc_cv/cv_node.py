import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np


class CVNode(Node):
    def __init__(self):
        super().__init__('cv_node')

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(Image, 'image_raw', self.process_image, 10)

        self.publisher = self.create_publisher(Image, 'image_processed', 10)

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
        
        self.get_logger().info("CV Node Started")

def process_image(self, msg):
    # Convert ROS image to OpenCV
    frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blur = cv2.GaussianBlur(
        gray,
        (self.blur_kernel_size, self.blur_kernel_size),
        self.blur_sigma_x,
        self.blur_sigma_y
    )

    # Canny edge detection
    edges = cv2.Canny(
        blur,
        self.canny_low,
        self.canny_high
    )
    
    # Hough Line Transform
    lines = cv2.HoughLinesP(
        edges,
        self.hough_rho,
        self.hough_theta,
        self.hough_threshold,
        minLineLength=self.hough_min_line_length,
        maxLineGap=self.hough_max_line_gap
    )

    line_image = np.zeros_like(frame)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 255), self.line_thickness)
    result = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    ros_image = self.bridge.cv2_to_imgmsg(result, 'bgr8')
    self.publisher.publish(ros_image)


def main(args=None):
    rclpy.init(args=args)
    node = CVNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()