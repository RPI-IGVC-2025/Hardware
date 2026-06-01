import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    single_gps_goal_node = Node(
        package="igvc_goal",
        executable="single_gps_goal_node",
        name="single_gps_goal_node",
        output="screen",
        parameters=[{
            "latitude": 42.66797627,
            "longitude": -83.21844458,
            "altitude": 0.0,
            "yaw": 0.0,
            "require_enabled": True,
        }],
    )

    return LaunchDescription([
        single_gps_goal_node
    ])
