#!/usr/bin/env python3

import rclpy
import math 
from rclpy.node import Node

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped, Quaternion
# from rclpy.action import ActionClient

# this node publishes to /goal_update on PoseStamped, which is 
# part of the geometry_msgs package. Nav2 subscribes to PoseStamped
# to determine next points 

#helper to convert angle to quaternion
def yaw_to_quaternion(yaw):
    q = Quaternion()
    q.x = 0.0
    q.y = 0.0
    q.z = math.sin(yaw / 2.0)
    q.w = math.cos(yaw / 2.0)
    return q
class GoalSettingNode(Node):
    def __init__(self):
        super().__init__('goal_setting_node')

        self.left_boundary = None
        self.right_boundary = None
        
        self.lookahead = 5
        self.goal_frame = 'base_footprint' #TODO need to verify

        self.create_subscription(Path, '/left_boundary', self.left_callback, 10)
        self.create_subscription(Path, '/right_boundary', self.right_callback, 10)

        self.goal_pub = self.create_publisher(PoseStamped, '/goal_pose', 10)

        self.create_timer(1.0, self.publish_goal)

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
        
        left_ahead_point = min(self.lookahead, len(self.left_boundary.poses) - 1)
        right_ahead_point = min(self.lookahead, len(self.right_boundary.poses) - 1)
        
        # get (x,y) coordinates for left and right boundaries
        left_pt = self.left_boundary.poses[left_ahead_point].pose.position
        right_pt = self.right_boundary.poses[right_ahead_point].pose.position
        
        
        mid_x = (left_pt.x + right_pt.x) / 2.0
        mid_y = (left_pt.y + right_pt.y) / 2.0
        
        #find further ahead midpoint to determine heading 
        heading_lookahead_left = min(left_ahead_point + 2, len(self.left_boundary.poses) - 1)
        heading_lookahead_right = min(right_ahead_point + 2, len(self.right_boundary.poses) - 1)

        left_ahead = self.left_boundary.poses[heading_lookahead_left].pose.position
        right_ahead = self.right_boundary.poses[heading_lookahead_right].pose.position

        next_mid_x = (left_ahead.x + right_ahead.x) / 2.0
        next_mid_y = (left_ahead.y + right_ahead.y) / 2.0

        # determine heading, calculate heading angle 
        yaw = math.atan2(next_mid_y - mid_y, next_mid_x - mid_x)
        #convert to ROS Quaternion (need an x, y, z, w)
        q = yaw_to_quaternion(yaw)
        
        # set the goal --> find the basic "halfway" point to determine path for now
        goal = PoseStamped()
        goal.header.stamp = self.get_clock().now().to_msg()
        goal.header.frame_id = self.goal_frame
        
        goal.pose.position.x = mid_x
        goal.pose.position.y = mid_y

        goal.pose.position.z = 0.0
        goal.pose.orientation = q


        self.goal_pub.publish(goal)
        
        
        self.get_logger().info(
            f'Sent Goal: ({goal.pose.position.x}, {goal.pose.position.y})'
        )
        
    


def main(args=None):
    rclpy.init(args=args)
    node = GoalSettingNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()