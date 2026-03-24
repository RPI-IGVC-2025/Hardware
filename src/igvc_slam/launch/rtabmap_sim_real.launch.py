import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

use_sim = False  # Switch to change mode

def generate_launch_description():
    rtabmap_package = get_package_share_directory('rtabmap_launch')
    zed_wrapper = get_package_share_directory('zed_wrapper')

    rtabmap_launch_path = os.path.join(rtabmap_package, 'launch', 'rtabmap.launch.py')
    zed_launch_path = os.path.join(zed_wrapper, 'launch', 'zed2i.launch.py')

    imu_filter = Node(
        package='imu_filter_madgwick', 
        executable='imu_filter_madgwick_node',
        output='screen',
        remappings=[
            ('/imu/data_raw', '/camera/camera/imu'),
            ('imu/data', '/rtabmap/imu')
        ],
        parameters=[
            {'use_mag' : False},
            {'publish_tf' : True},
            {'fixed_frame' : 'camera_link'}
        ]
    )

    rtabmap_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rtabmap_launch_path),
        launch_arguments={
            'args' : '--delete_db_on_start',
            'depth_topic' : '/zed/zed_node/depth/depth_registered',
            'rgb_topic' : '/zed/zed_node/rgb/image_rect_color',
            'camera_info_topic' : '/zed/zed_node/rgb/camera_info',
            'approx_sync' : 'true',
            'frame_id' : 'base_footprint',
            'log_level' : 'debug', 
            'publish_tf_odom' : 'true',
            'odom_topic' : '/zed/zed_node/odom',
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

    rtabmap_real = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rtabmap_launch_path),
        launch_arguments={
            'args' : '--delete_db_on_start',
            'depth_topic' : '/zed/zed_node/depth/depth_registered',
            'rgb_topic' : '/zed/zed_node/rgb/image_rect_color',
            'camera_info_topic' : '/zed/zed_node/rgb/camera_info',
            'frame_id' : 'base_footprint',
            'publish_tf_odom' : 'true',
            'odom_topic' : '/zed/zed_node/odom',
            'odom_frame_id' : 'odom',
	        'approx_sync' : 'true',
            'rgbd_sync' : 'true',
	        'approx_rgbd_sync' : 'true',
            'subscribe_rgbd' : 'true',
            'visual_odometry' : 'true',
            'qos' : '1',
            'approx_sync_max_interval' : '0.01',
	        'sync_queue_size' : '50',
	        'topic_queue_size' : '50',  
            'wait_for_transform' : '0.4',
            'imu_topic' : '/rtabmap/imu',
            'wait_imu_to_init' : 'true',
	        'rtabmap_viz' : 'true',
            'map_topic' : '/map'
        }.items()
    )

    zed_camera = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(zed_launch_path),
        launch_arguments={
            'enable_color' : 'true',
            'enable_depth' : 'true',
            'align_depth.enable' : 'true', 
            'pointcloud.enable' : 'false',
            'enable_sync' : 'false',
            'unite_imu_method' : '2',
            'enable_gyro' : 'true',
            'enable_accel' : 'true',
            'color_fps' : '60',
            'depth_fps' : '60', 
            'gyro_fps' : '200',
            'accel_fps' : '63',
            'publish_tf' : 'true'
        }.items()
    )

    if use_sim == False:
        return LaunchDescription([
            imu_filter,
            rtabmap_real,
            zed_camera
        ])
    else:
        return LaunchDescription([
            rtabmap_sim,
        ])