from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    use_sim_gpio = LaunchConfiguration("use_sim_gpio")
    
    twist_mux_config = PathJoinSubstitution([
        FindPackageShare("igvc_estop"),
        "config",
        "twist_mux.yaml",
    ])

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim_gpio",
            default_value="false",
            description="Use sim GPIO topic instead of Jetson GPIO",
        ),
    
        Node(
            package="twist_mux",
            executable="twist_mux",
            name="twist_mux",
            output="screen",
            parameters=[twist_mux_config],
            remappings=[
                # twist_mux output topic -> controller cmd_vel input
                ("cmd_vel_out", "/cmd_vel_unstamped"),
            ],
        ),
        
        Node(
            package="twist_stamper",
            executable="twist_stamper",
            name="twist_stamper",
            output="screen",
            remappings=[
                ("cmd_vel_in", "/cmd_vel_unstamped"),
                ("cmd_vel_out", "/bot_drive_controller/cmd_vel"),
            ],
        ),

        Node(
            package="igvc_estop",
            executable="igvc_estop_node",
            name="igvc_estop",
            output="screen",
            parameters=[{
                "use_sim_gpio": use_sim_gpio,
                "sim_gpio_topic": "/sim_gpio_estop",

                "gpio_pin": 27,
                "gpio_mode": "BCM",
                "active_high": True,

                "mechanical_estop_pin": 22,
                "mechanical_active_low": True,

                "latch": True,
                "poll_hz": 50.0,

                "lock_topic": "/emergency_stop_lock",
                "reset_topic": "/emergency_stop_reset",
            }],
        ),
    ])
