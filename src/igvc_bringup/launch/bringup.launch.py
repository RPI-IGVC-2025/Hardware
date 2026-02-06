from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim = LaunchConfiguration('use_sim')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim',
            default_value='true',
            description='Run in Gazebo'
        ),

        # Robot description (URDF)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_bringup'),
                 '/launch/description.launch.py']
            )
        ),

        # Simulation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_bringup'), '/launch/gazebo.launch.py']
            ),
            condition=IfCondition(use_sim),
        ),

        # Control
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_bringup'),
                 '/launch/hardware.launch.py']
            ),
            condition=IfCondition(use_sim),
        ),

        # Real hardware
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_bringup'),
                 '/launch/hardware.launch.py']
            ),
            condition=UnlessCondition(use_sim),
        ),

        # SLAM
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_bringup'),
                 '/launch/slam.launch.py']
            )
        ),

        # Navigation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_bringup'),
                 '/launch/nav.launch.py']
            )
        ),
    ])
