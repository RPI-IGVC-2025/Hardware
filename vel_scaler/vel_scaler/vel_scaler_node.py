#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CmdVelScaler(Node):
    def __init__(self):
        super().__init__("cmd_vel_scaler")

        self.declare_parameter("input_topic", "/cmd_vel")
        self.declare_parameter("output_topic", "/cmd_vel_scaled")
        self.declare_parameter("linear_scale", 1.0)
        self.declare_parameter("angular_scale", 1.0)

        input_topic = self.get_parameter("input_topic").value
        output_topic = self.get_parameter("output_topic").value

        self.linear_scale = float(self.get_parameter("linear_scale").value)
        self.angular_scale = float(self.get_parameter("angular_scale").value)

        self.sub = self.create_subscription(
            Twist,
            input_topic,
            self.cmd_vel_callback,
            10,
        )

        self.pub = self.create_publisher(
            Twist,
            output_topic,
            10,
        )

        self.get_logger().info(
            f"Scaling {input_topic} -> {output_topic} "
            f"with linear_scale={self.linear_scale}, angular_scale={self.angular_scale}"
        )

    def cmd_vel_callback(self, msg: Twist):
        scaled = Twist()

        scaled.linear.x = msg.linear.x * self.linear_scale
        scaled.linear.y = msg.linear.y * self.linear_scale
        scaled.linear.z = msg.linear.z * self.linear_scale

        scaled.angular.x = msg.angular.x * self.angular_scale
        scaled.angular.y = msg.angular.y * self.angular_scale
        scaled.angular.z = msg.angular.z * self.angular_scale

        self.pub.publish(scaled)


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelScaler()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()