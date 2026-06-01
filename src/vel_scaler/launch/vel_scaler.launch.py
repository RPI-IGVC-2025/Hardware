from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="vel_scaler",
            executable="vel_scaler_node",
            name="cmd_vel_scaler",
            output="screen",
            parameters=[{
                "input_topic": "/cmd_vel",
                "output_topic": "/cmd_vel_scaled",
                "linear_scale": 6.35242261,
                "angular_scale": -20.0,
            }],
        )
    ])
