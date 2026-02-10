from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument


def generate_launch_description():
    # scenario = 
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'scenario',
            default_value='empty_world',
            description='Simulation Scenario'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [
                FindPackageShare('igvc_gazebo'),
                 '/launch/',
                 LaunchConfiguration('scenario'),
                 '.launch.py'
                ]
            )
        )
    ])
