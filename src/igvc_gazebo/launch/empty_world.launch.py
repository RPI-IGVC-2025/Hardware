import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

from launch_ros.actions import Node

import xacro

def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    pkg_description = FindPackageShare(package='igvc_description').find('igvc_description')

    gz_launch_path = os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
    publisher_launch_path = os.path.join(pkg_description, 'launch/publisher.launch.py')

    world = LaunchConfiguration('world')

    default_world = os.path.join(
        get_package_share_directory('igvc_gazebo'),
        'worlds',
        'empty_world.sdf'
    )

    world_arg = DeclareLaunchArgument(
        'world',
        default_value=default_world,
        description='World to load'
    )

    gazebo = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_launch_path),
            launch_arguments={'gz_args': ['-r -v4 ', world], 'on_exit_shutdown': 'true'}.items()
        )

    start_publisher_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(publisher_launch_path)
    )
    
    spawn_entity = Node(package='ros_gz_sim', executable='create',
        arguments=['-topic', 'robot_description',
                    '-name', 'igvc_robot'],
        output='screen'
    )

    bridge_params = os.path.join(get_package_share_directory('igvc_gazebo'), 'config', 'gz_bridge.yaml')
    
    ros_gz_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}',
        ]
    )
    
    return LaunchDescription([
        world_arg,
        gazebo,
        start_publisher_cmd,
        spawn_entity,
        ros_gz_bridge
    ])
