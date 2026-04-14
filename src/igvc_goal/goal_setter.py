#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

# this node publishes to /goal_update on PoseStamped, which is 
# part of the geometry_msgs package. Nav2 subscribes to PoseStamped
# to determine next points 
class GoalSettingNode(Node):
    def __init__(self):
        super().__init__('goal_setting_node')

        self.left_boundary = None
        self.right_boundary = None

        self.create_subscription(Path, '/left_boundary', self.left_callback, 10)
        self.create_subscription(Path, '/right_boundary', self.right_callback, 10)

        self.goal_pub = self.create_publisher(PoseStamped, '/goal_update', 10)

        self.create_timer(0.1, self.publish_goal)

    # subscribe to /left_boundary
    def left_callback(self, msg):
        self.left_boundary = msg

    # subscribe to /right_boundary
    def right_callback(self, msg):
        self.right_boundary = msg

    # publish goal to nav2
    def publish_goal(self):
        if self.left_boundary is None or self.right_boundary is None:
            return

        goal = PoseStamped()
        goal.header.stamp = self.get_clock().now().to_msg()
        goal.header.frame_id = 'base_footprint'

        # placeholder goal
        goal.pose.position.x = 1.0
        goal.pose.position.y = 0.0
        goal.pose.position.z = 0.0
        goal.pose.orientation.w = 1.0

        self.goal_pub.publish(goal)


def main(args=None):
    rclpy.init(args=args)
    node = GoalSettingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()