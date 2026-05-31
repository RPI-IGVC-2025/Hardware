from compass_driver import Compass

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class CompassNode(Node):
    def __init__(self):
        super().__init__('compass_bridge')
        self.get_logger().info("compass bridge started")

        self.declare_parameter('i2c_bus')
        self.declare_parameter('device_address')
        self.declare_parameter('config_filepath')

        # Create Compass
        self._instance = Compass(
            i2c_bus=self.get_parameter('i2c_bus').get_parameter_value().integer,
            address=self.get_parameter('device_address').get_parameter_value().integer,
            CONFIG_FILEPATH=self.get_parameter('config_filepath').get_parameter_value().string
        )

        # Create Publisher
        self.publisher_ = self.create_publisher(Float32, 'compass_heading', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def cleanup(self):
        try:
            self._instance.cleanup()
        except Exception as e:
            self.get_logger().error(f"Error during cleanup: {e}")

    def timer_callback(self):
        try:
            heading = self._instance.get_heading()
            msg = Float32()
            msg.data = heading
            self.publisher_.publish(msg)
        except Exception as e:
            self.get_logger().error(f"Error in timer callback: {e}")


    
def main(args=None):
    try:
        rclpy.init(args=args)
        node = CompassNode()
        rclpy.spin(node)
    finally:
        node.cleanup()
        node.destroy_node()
        rclpy.shutdown()
    

if __name__ == '__main__':
    main()
