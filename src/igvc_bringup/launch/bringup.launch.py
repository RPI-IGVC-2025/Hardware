import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription, LaunchDescriptionSource
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import FrontendLaunchDescriptionSource, PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim = LaunchConfiguration('use_sim')
    use_mock_hardware = LaunchConfiguration('use_mock_hardware')
    
    return LaunchDescription([
        # Launch Arguments
        DeclareLaunchArgument(
            'use_sim',
            default_value='false',
            description='Run in Simulation'
        ),
        DeclareLaunchArgument(
            'sim_world',
            default_value='track_v1',
            description='The name of the scenario to open in Gazebo'
        ),
        DeclareLaunchArgument(
            'use_mock_hardware',
            default_value=use_sim, # You are always mocking in simulation, but can specify if you need to bypass physical descriptors for testing
            description='Mocks all hardware'
        ),
        
        DeclareLaunchArgument(
            'use_slam',
            default_value='true', 
            description='Launch rtabmap for SLAM'
        ),


        #Estop
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_estop'),
                 '/launch',
                 '/igvc_estop.launch.py']
            ),
            launch_arguments={
                'use_sim_gpio': use_sim
            }.items()
        ),

        # Publishers & URDF
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_description'),
                 '/launch',
                 '/publisher.launch.py']
            ),
            launch_arguments={
                'use_mock_hardware': use_mock_hardware
                }.items()
        ),

        # Simulation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_gazebo'),
                 '/launch/',
                 LaunchConfiguration('sim_world'),
                 '.launch.py'
                ]
            ),
            condition=IfCondition(use_sim),
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
            condition = UnlessCondition(use_mock_hardware)
        ),
        
        # SLAM
        IncludeLaunchDescription(        
            FrontendLaunchDescriptionSource(
                [FindPackageShare('igvc_slam'),
                '/launch',
                '/igvc_slam.launch']
            ),     
            condition = IfCondition(LaunchConfiguration('use_slam'))
        )
    ])
