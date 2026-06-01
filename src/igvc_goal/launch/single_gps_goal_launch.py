import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    single_gps_goal_node = Node(
        package="your_package",
        executable="single_gps_goal_node",
        name="single_gps_goal_node",
        output="screen",
        parameters=[{
            "latitude": 42.66823105,
            "longitude": -83.21846028,
            "altitude": 0.0,
            "yaw": 0.0,
            "require_enabled": True,
        }],
    )

    return LaunchDescription([
        single_gps_goal_node
    ])
