from launch import LaunchDescription
from launch.substitutions import  PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

IMU_NAME = "TODO" # TODO

def generate_launch_description():
    # Declare args
    launch_zed_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("zed_wrapper"),
             '/launch',
             'camera.launch.py']
        ),
        launch_arguments={
            'camera_model:=zed2i'
        }
    )
    # Check here for published topics: https://www.stereolabs.com/docs/ros2/zed-node
    
    launch_rplidar_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [FindPackageShare("rplidar_ros"),
             '/launch',
             'rplidar_s2e_launch.py']
        ),
        launch_arguments={
            # TODO if we want to change anything
        }
    )

    declared_arguments = [
        launch_zed_node,
        launch_rplidar_node
    ]
    
    # Get nodes    
    imu_node = Node(
        package="adi_imu",
        executable="adi_imu_node",
        ros_arguments=["-p", f"imu_device_name:=${IMU_NAME}"]
    )
    nodes = [
        imu_node
    ]

    return LaunchDescription(declared_arguments + nodes)