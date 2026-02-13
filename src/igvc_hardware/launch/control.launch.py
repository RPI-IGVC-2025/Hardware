from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    # Declare args
    declared_arguments = []
    
    # Get nodes
    robot_controllers = PathJoinSubstitution(
        [
            FindPackageShare("igvc_hardware"),
            "config",
            "bot_controllers.yaml",
        ]
    )

    control_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[
            # TODO in the ODrive botwheel explorer example, the description contents are also passed in here.
            robot_controllers
        ],
        output="both",
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["bot_drive_controller",
                   "--controller-manager", "/controller_manager"],
    )

    nodes = [
        control_node,
        robot_controller_spawner
    ]

    return LaunchDescription(declared_arguments + nodes)
