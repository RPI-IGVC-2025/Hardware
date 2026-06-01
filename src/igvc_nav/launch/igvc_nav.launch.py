import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    nav2_bringup_package  = get_package_share_directory('nav2_bringup')
    igvc_nav_package = get_package_share_directory('igvc_nav')
    vel_scaler_package = get_package_share_directory('vel_scaler')

    nav2_launch_path = os.path.join(nav2_bringup_package , 'launch', 'navigation_launch.py')
    config_path = os.path.join(igvc_nav_package, 'config', 'nav2_params.yaml')
    vel_scaler_launch_path = os.path.join(igvc_nav_package, 'launch', 'vel_scaler.launch.py')

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(nav2_launch_path),
        launch_arguments={
            'params_file' : config_path
        }.items()
    )
    
    # vel_scaler = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(vel_scaler_launch_path)
    # )

    return LaunchDescription([
        nav2,
        # vel_scaler
    ])