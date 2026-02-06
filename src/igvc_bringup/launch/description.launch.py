from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_description'),
                 '/launch/publisher.launch.py']
            )
        )
    ])
