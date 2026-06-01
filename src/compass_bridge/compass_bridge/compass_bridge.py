from .compass_driver import Compass

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from sensor_msgs.msg import Imu
import sys
import math

class CompassNode(Node):
    def __init__(self):
        super().__init__('compass_bridge')
        self.get_logger().info("compass bridge started")

        self.declare_parameter('i2c_bus', 7)
        self.declare_parameter('device_address', 0x0E)
        self.declare_parameter('config_filepath', '/home/rpirobo3/2026RobotCode/src/igvc_hardware/config/compass_config.yaml')
        
        # Create Compass
        self._instance = Compass(
            i2c_bus=self.get_parameter('i2c_bus').get_parameter_value().integer_value,
            address=self.get_parameter('device_address').get_parameter_value().integer_value,
            CONFIG_FILEPATH=self.get_parameter('config_filepath').get_parameter_value().string_value,
            logger=self.get_logger()
        )

        # Create Publisher
        self.publisher_ = self.create_publisher(Float32, 'compass_heading', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def cleanup(self):
        try:
            self._instance.cleanup()
        except Exception as e:
            self.get_logger().error(f"Error during cleanup: {e}")

    def timer_callback(self):
        try:
            heading = self._instance.get_heading()
            if heading is not None:
                heading_yaw = math.radians(heading)
                imu_msg = Imu()
                imu_msg.header.stamp = self.get_clock().now().to_msg()
                imu_msg.header.frame_id = 'imu_link'
                
                q = tf_transformations.quaternion_from_euler(0, 0, heading_yaw)
                
                imu_msg.orientation.x = q[0]
                imu_msg.orientation.y = q[1]
                imu_msg.orientation.z = q[2]
                imu_msg.orientation.w = q[3]
                        
                imu_msg.orientation_covariance[0] = -1.0
                imu_msg.angular_velocity_covariance[0] = -1.0
                imu_msg.linear_acceleration_covariance[0] = -1.0
        
                self.publisher_.publish(imu_msg)

        except Exception as e:
            self.get_logger().error(f"Error in timer callback: {e}")


    
def main(args=None):
    try:
        rclpy.init(args=args)
        node = None
        node = CompassNode()
        rclpy.spin(node)
    finally:
        if node is not None:
            node.cleanup()
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
    

if __name__ == '__main__':
    main()
