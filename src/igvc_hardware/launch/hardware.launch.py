from launch import LaunchDescription
from launch.substitutions import  PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

IMU_NAME = "TODO" # TODO

def generate_launch_description():
    # Declare args
    declared_arguments = []
    
    # Get nodes    
    imu_node = Node(
        package="adi_imu",
        executable="adi_imu_node",
        ros_arguments=["-p", f"imu_device_name:=${IMU_NAME}"]
    )

    # TODO zed (camera)

    # TODO In the examples, the controller manager is not spawned until the joint state broadcaster is finished spawning. Implement if we have problems regarding that.
    
    nodes = [
        imu_node
    ]

    return LaunchDescription(declared_arguments + nodes)