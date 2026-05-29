from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    twist_mux_config = PathJoinSubstitution([
        FindPackageShare("gpio_estop"),
        "config",
        "twist_mux.yaml",
    ])

    return LaunchDescription([
        Node(
            package="twist_mux",
            executable="twist_mux",
            name="twist_mux",
            output="screen",
            parameters=[twist_mux_config],
            remappings=[
                # twist_mux output topic -> controller cmd_vel input
                ("cmd_vel_out", "/cmd_vel"),
            ],
        ),

        Node(
            package="gpio_estop",
            executable="gpio_estop_node",
            name="gpio_estop",
            output="screen",
            parameters=[{
                "gpio_pin": 7,
                "gpio_mode": "BOARD",
                "active_high": True,
                "latch": True,
                "poll_hz": 50.0,
                "lock_topic": "/emergency_stop_lock",
                "reset_topic": "/emergency_stop_reset",
            }],
        ),
    ])