import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    lane_points_node = Node(
        package='igvc_cv',
        executable='lane_points_node',
        name='lane_points_node',
        output='screen',
        parameters=[{
            'image_topic': '/zed/zed_node/rgb/color/rect/image',
            'cloud_topic': '/zed/zed_node/point_cloud/cloud_registered',
            'output_topic': '/lanes/points',
            'roi_top_fraction': 0.25,
            'min_value': 120,
            'max_saturation': 180,
            'pixel_stride': 1,
            'max_points': 8000,
            'min_depth_m': 0.2,
            'max_depth_m': 12.0,
            'max_abs_x_m': 20.0,
            'max_abs_y_m': 20.0,
        }]
    )

    return LaunchDescription([
        lane_points_node
    ])