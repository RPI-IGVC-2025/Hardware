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

        self.subscription = self.create_subscription(Image, 'image_raw', self.image_callback, 10)

        self.publisher = self.create_publisher(Image, 'image_processed', 10)

        self.get_logger().info("CV Node Started")

    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (11, 11), 33)
        edges = cv2.Canny(blur, 50, 150)

        lines = cv2.HoughLinesP(edges, 2, np.pi / 180, 50, minLineLength=30, maxLineGap=10)

        line_image = np.zeros_like(frame)

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line.reshape(4)
                cv2.line(line_image, (x1, y1), (x2, y2),
                         (0, 255, 255), 3)

        result = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

        ros_image = self.bridge.cv2_to_imgmsg(result, 'bgr8')
        self.publisher.publish(ros_image)


def main(args=None):
    rclpy.init(args=args)
    node = CVNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()