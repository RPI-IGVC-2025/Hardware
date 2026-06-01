import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

#!/usr/bin/env python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory("igvc_cv")

    params_file = os.path.join(
        pkg_share,
        "config",
        "lane_points.yaml",
    )

    lane_points_node = Node(
        package="igvc_cv",
        executable="lane_points_node",
        name="lane_points_node",
        output="screen",
        parameters=[params_file],
    )

    return LaunchDescription([
        lane_points_node,
    ])
