import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    declared_arguments = []
    package_description = FindPackageShare(package='igvc_description').find('igvc_description')
    ros_gz_sim_package = get_package_share_directory('ros_gz_sim')
    gz_launch_path = os.path.join(ros_gz_sim_package, 'launch', 'gz_sim.launch.py')
    world = LaunchConfiguration('world')
    bridge_params = os.path.join(get_package_share_directory('igvc_gazebo'), 'config', 'gz_bridge.yaml')
    default_world = os.path.join(get_package_share_directory('igvc_gazebo'), 'worlds','empty_world.sdf')

    declared_arguments.append(
        DeclareLaunchArgument(
            'world',
            default_value=default_world,
            description='World to load'
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'gazebo',
            PythonLaunchDescriptionSource(gz_launch_path),
            launch_arguments={'gz_args': ['-r -v4 ', world], 'on_exit_shutdown': 'true'}.items()
        )
    )

    spawn_entity = Node(
        package='ros_gz_sim', executable='create',
        arguments=[
            '-topic', 
            'robot_description',
            '-name', 
            'igvc_robot'
        ],
        output='screen'
    )

    ros_gz_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}',
        ]
    )
    
    Nodes = [
        spawn_entity,
        ros_gz_bridge
    ]
    
    return LaunchDescription(declared_arguments + Nodes)  