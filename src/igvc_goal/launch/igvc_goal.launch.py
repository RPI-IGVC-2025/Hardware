import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    lane_director_node = Node(
        package='igvc_goal',
        executable='lane_director_node',
        name='lane_director_node',
        output='screen',
        parameters=[{
            'enabled_topic': '/enabled',
            'lane_points_topic': '/lanes/points',
            'base_frame': 'base_link',
            'global_frame': 'map',
            'goal_period_s': 1.0,
            'lookahead_distance_m': 3.0,
            'nominal_lane_width_m': 1.2,
        }],
    )

    return LaunchDescription([
        lane_director_node
    ])