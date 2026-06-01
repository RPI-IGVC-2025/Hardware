import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    igvc_slam_package = get_package_share_directory('igvc_slam')
    param_file = os.path.join(igvc_slam_package, 'config', 'dual_ekf_params.yaml')

    ekf_node_odom = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_node_odom',
        output='screen',
        parameters=[param_file],
        remappings=[('odometry/filtered', '/odometry/local')],
    )
    
    ekf_node_map = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_node_map',
        output='screen',
        parameters=[param_file],
        remappings=[('odometry/filtered', '/odometry/global')],
    )
    
    navsat_transform = Node( 
        package='robot_localization',
        executable='navsat_transform_node',
        name='navsat_transform',
        output='screen',
        parameters=[param_file],
        remappings=[
            ('imu', '/zed/zed_node/imu/data'), #TODO: change to compass imu
            ('gps/fix', '/fix'),
            ('gps/filtered', '/gps/filtered'),
            ('odometry/gps', '/odometry/gps'),
            ("odometry/filtered", "/odometry/local"),
        ],
    )

    return LaunchDescription([
        ekf_node_odom,
        ekf_node_map,
        navsat_transform
    ])
