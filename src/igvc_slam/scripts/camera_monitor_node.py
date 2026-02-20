# This is a subscriber file (input).

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image


class CameraMonitorNode(Node):

    def __init__(self):
        super().__init__('camera_monitor_node')
        self.subscription = self.create_subscription(
            Image,
            '/camera/camera/color/image_raw',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    # self.get_logger() gets the logger for this node.
    # info() is similar to print(), but uses ROS2 logging.
    # str() converts non-string values (e.g., integers) to strings
    # so we can use +
    def listener_callback(self, msg):
        self.get_logger().info("width=" + str(msg.width) + ", height=" + str(msg.height) + ", encoding=" + str(msg.encoding) + ", frame_id=" + str(msg.header.frame_id))


def main(args=None):
    rclpy.init(args=args)

    camera_monitor_node = CameraMonitorNode()

    rclpy.spin(camera_monitor_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    camera_monitor_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()