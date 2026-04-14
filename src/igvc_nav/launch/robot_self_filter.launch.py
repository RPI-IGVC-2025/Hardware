import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    igvc_nav_share = get_package_share_directory('igvc_nav')
    igvc_description_share = get_package_share_directory('igvc_description')

    default_urdf = os.path.join(igvc_description_share, 'urdf', 'robot.urdf.xacro')
    filter_config = os.path.join(igvc_nav_share, 'config', 'robot_self_filter.yaml')

    urdf_model = LaunchConfiguration('urdf_model')
    use_mock_hardware = LaunchConfiguration('use_mock_hardware')
    use_sim_time = LaunchConfiguration('use_sim_time')

    robot_description = ParameterValue(
        Command(['xacro ', urdf_model, ' use_mock_hardware:=', use_mock_hardware]),
        value_type=str,
    )

    self_filter_node = Node(
        package='robot_self_filter',
        executable='self_filter',
        name='self_filter',
        output='screen',
        parameters=[
            filter_config,
            {
                'robot_description': robot_description,
                'use_sim_time': use_sim_time,
                'lidar_sensor_type': 0,
                'zero_for_removed_points': False,
            },
        ],
        remappings=[
            ('/cloud_in', LaunchConfiguration('in_pointcloud_topic')),
            ('/cloud_out', LaunchConfiguration('out_pointcloud_topic')),
        ],
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                'urdf_model',
                default_value=default_urdf,
                description='Path to robot xacro (same as igvc_description publisher)',
            ),
            DeclareLaunchArgument(
                'use_mock_hardware',
                default_value='false',
                description='Forwarded to xacro (must match robot_state_publisher)',
            ),
            DeclareLaunchArgument(
                'use_sim_time',
                default_value='true',
                description='Must match simulation clock when using Gazebo',
            ),
            DeclareLaunchArgument(
                'in_pointcloud_topic',
                default_value='/scan/points',
                description='Raw lidar point cloud from bridge or driver',
            ),
            DeclareLaunchArgument(
                'out_pointcloud_topic',
                default_value='/scan/points_filtered',
                description='Self-filtered cloud for Nav2 / collision_monitor',
            ),
            self_filter_node,
        ]
    )
