import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition

def generate_launch_description():
    nav2_bringup_package  = get_package_share_directory('nav2_bringup')
    igvc_nav_package = get_package_share_directory('igvc_nav')

    nav2_launch_path = os.path.join(nav2_bringup_package , 'launch', 'navigation_launch.py')
    config_path = os.path.join(igvc_nav_package, 'config', 'nav2_params.yaml')
    self_filter_launch = os.path.join(igvc_nav_package, 'launch', 'robot_self_filter.launch.py')
    
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_mock_hardware = LaunchConfiguration('use_mock_hardware')

    self_filter = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(self_filter_launch),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'use_mock_hardware': use_mock_hardware,
        }.items(),
        condition=IfCondition(LaunchConfiguration('enable_robot_self_filter')),
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_path),
        launch_arguments={
            'params_file' : config_path,
            'use_sim_time' : use_sim_time,
        }.items()
        
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true'
        ),
        DeclareLaunchArgument(
            'use_mock_hardware',
            default_value='false',
            description='Must match igvc_description publisher xacro arg',
        ),
        DeclareLaunchArgument(
            'enable_robot_self_filter',
            default_value='true',
            description='Publish /scan/points_filtered for Nav2 collision_monitor',
        ),

        self_filter,
        nav2
    ])