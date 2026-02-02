import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

def generate_launch_description():
    imu_filter = Node(
        package='imu_filter_madgwick', 
        executable='imu_filter_madgwick_node',
        output='screen',
        remappings=[
            ('/imu/data_raw', '/imu_plugin/out'),
            ('imu/data', '/rtabmap/imu')
        ],
        parameters=[
            {'use_mag' : False},
            {'publish_tf' : False},
            {'fixed_frame' : 'imu_link'}
        ]
    )
        
    rtabmap_package = get_package_share_directory('rtabmap_launch')

    rtabmap_launch_path = os.path.join(rtabmap_package, 'launch', 'rtabmap.launch.py')

    rtabmap = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rtabmap_launch_path),
        launch_arguments={
            'args' : '--delete_db_on_start',
            'depth_topic' : '/camera/camera/depth/image_rect_raw',
            'rgb_topic' : '/camera/camera/color/image_raw',
            'camera_info_topic' : '/camera/camera/depth/camera_info',
            'approx_sync' : 'true',
            'frame_id' : 'base_footprint',
            'log_level' : 'debug', 
            'publish_tf_odom' : 'false',
            'odom_topic' : '/odom',
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
            'wait_imu_to_init' : 'true',
            'map_topic' : '/map'
        }.items()
    )

    return LaunchDescription([
        imu_filter,
        rtabmap
    ])