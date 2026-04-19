from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    declared_arguments = []

    declared_arguments.append(
        DeclareLaunchArgument(
            'world',
            default_value=PathJoinSubstitution([
                FindPackageShare('igvc_gazebo'),
                'worlds',
                'track_v1.sdf'
            ]),
            description='World to load'
        )
    )

    world = LaunchConfiguration('world')

    gz_sim_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            ])
        ),
        launch_arguments={
            'gz_args': ['-r -v4 ', world],
            'on_exit_shutdown': 'true'
        }.items()
    )

    spawn_entity_node = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', 'robot_description',
            '-name', 'igvc_robot'
        ],
        output='screen'
    )

    bridge_params = PathJoinSubstitution([
        FindPackageShare('igvc_gazebo'),
        'config',
        'gz_bridge.yaml'
    ])

    ros_gz_bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridge_params}'
        ]
    )

    Nodes = [
        gz_sim_description,
        spawn_entity_node,
        ros_gz_bridge_node
    ]

    return LaunchDescription(declared_arguments + Nodes)