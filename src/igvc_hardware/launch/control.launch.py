from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.event_handlers import OnProcessExit
from launch.actions import DeclareLaunchArgument, RegisterEventHandler

from launch.conditions import UnlessCondition

def generate_launch_description():
    # Declare args
    declared_arguments = []
    
    declared_arguments.append(
        DeclareLaunchArgument(
            name="use_sim",
            default_value="false",
            description="Wether or not the robot is launching in simulation"
        )
    )
    
    use_sim = LaunchConfiguration("use_sim")
    
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
        remappings=[
            ("~/robot_description", "/robot_description"),
        ],
        output="screen",
        condition = UnlessCondition(use_sim)
    )

    robot_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["bot_drive_controller",
                   "--controller-manager", "/controller_manager", "--switch-timeout", "20.0"],
        remappings=[
            ('~/cmd_vel','/cmd_vel'),
            ("~/robot_description", "/robot_description")
        ]
    )
    
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager", "--switch-timeout", "20.0"],
    )

    
    delay_robot_controller_spawner_after_joint_state_broadcaster_spawner = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[robot_controller_spawner],
        )
    )

    nodes = [
        control_node,
        joint_state_broadcaster_spawner,
        robot_controller_spawner
    ]

    return LaunchDescription(declared_arguments + nodes)
