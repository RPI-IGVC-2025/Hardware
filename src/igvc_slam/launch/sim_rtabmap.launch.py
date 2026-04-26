from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    declared_arguments = []

    rtabmap = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('rtabmap_launch'),
                'launch',
                'rtabmap.launch.py'
            ])
        ),
        launch_arguments={
            'args' : '--delete_db_on_start',
            'depth_topic' : '/camera/camera/depth/image_rect_raw',
            'rgb_topic' : '/camera/camera/color/image_raw',
            'camera_info_topic' : '/camera/camera/depth/camera_info',
            'approx_sync' : 'true',
            'frame_id' : 'base_link',
            'log_level' : 'debug', 
            'publish_tf_odom' : 'true',
            'odom_topic' : 'odom',
            'odom_frame_id' : 'odom',
            'sync_queue_size' : '10', #TODO verify
            'topic_queue_size' : '10', #TODO verify
            'rgbd_sync' : 'true',
            'approx_rgbd_sync' : 'true',
            'subscribe_depth' : 'false',
            'subscribe_rgbd' : 'true',
            'visual_odometry' : 'true',
            'approx_sync_max_interval' : '0.01',
            'qos' : '1',
            'rviz' : 'true',
            'use_sim_time' : 'true',
            'wait_for_transform' : '0.4',
            'imu_topic' : '/rtabmap/imu',
            'wait_imu_to_init' : 'false',
            'map_topic' : '/map'
        }.items()
    )

    Nodes = [
        rtabmap
    ]

    return LaunchDescription(declared_arguments + Nodes)
