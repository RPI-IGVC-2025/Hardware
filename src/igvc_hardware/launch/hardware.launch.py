from launch import LaunchDescription
from launch.substitutions import  PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

IMU_NAME = "TODO" # TODO

def generate_launch_description():
    # Declare args
    declared_arguments = []
    
    # Get nodes
    robot_controllers = PathJoinSubstitution(
        [
            FindPackageShare("hardware"),
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
        arguments=["bot_controller", "--controller-manager", "/controller_manager"],
    )
    
    imu_node = Node(
        package="adi_imu",
        executable="adi_imu_node",
        ros_arguments=["-p", f"imu_device_name:=${IMU_NAME}"]
    )

    # TODO depthai (camera)

    # TODO In the examples, the controller manager is not spawned until the joint state broadcaster is finished spawning. Implement if we have problems regarding that.
    
    nodes = [
        control_node,
        robot_controller_spawner
    ]

    return LaunchDescription(declared_arguments + nodes)