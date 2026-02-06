from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim = LaunchConfiguration('use_sim')
        
    return LaunchDescription([
        # Launch Arguments
        DeclareLaunchArgument(
            'use_sim',
            default_value='false',
            description='Run in Simulation'
        ),
        DeclareLaunchArgument(
            'sim_scenario',
            default_value='empty_world',
            description='The name of the scenario to open in Gazebo'
        ),

        # Publishers & URDF
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_description'),
                 '/launch',
                 '/publisher.launch.py']
            )
        ),

        # Simulation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_gazebo'), 
                 '/launch',
                 '/gazebo.launch.py']
            ),
            condition=IfCondition(use_sim),
            launch_arguments={
                'scenario': LaunchConfiguration('sim_scenario'), 
            }.items(),
        ),

        # ROS2_Control
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_hardware'),
                 '/launch',
                 '/control.launch.py']
            ),
        ),

        # Real hardware
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_hardware'),
                 '/launch',
                 '/hardware.launch.py']
            ),
            condition = UnlessCondition(use_sim)
        ),

        # SLAM
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_slam'),
                 '/launch',
                 '/rtabmap.launch.py']
            ),
        ),

        # Navigation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_nav'),
                 '/launch',
                 '/igvc_nav.launch.py']
            ),
        ),
    ])
