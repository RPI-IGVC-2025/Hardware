# WORK FILE

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

from launch_ros.actions import Node

def generate_launch_description():
    rtabmap_package = get_package_share_directory('rtabmap_launch')
    package_slam = FindPackageShare(package='igvc_slam').find('igvc_slam')

    rtabmap_launch_path = os.path.join(rtabmap_package, 'launch', 'rtabmap.launch.py')

    rtabmap = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(rtabmap_launch_path),
        launch_arguments={
            'args' : '--delete_db_on_start',
            # Topics
            'depth_topic' : '/camera/camera/depth/image_rect_raw',
            'rgb_topic' : '/camera/camera/color/image_raw',
            'camera_info_topic' : '/camera/camera/depth/camera_info',
            'imu_topic' : '/rtabmap/imu', # Placeholder path
            'gps_topic' : '/rtabmap/gps', # Placeholder path
            'odom_topic' : '/odom',
            'scan_topic' : '/scan', # LiDAR placeholder
            
            # Camera Arguments
            'frame_id' : 'base_footprint',
            'rgbd_sync' : 'true',
	        'approx_rgbd_sync' : 'true',
            'approx_sync_max_interval' : '0.01',
            'subscribe_rgbd' : 'true',
            'subscribe_depth' : 'false',
            
            # Odometry Arguments
            'odom_frame_id' : 'odom',
            'publish_tf_odom' : 'true',
            'icp_odometry' : 'true', # Lidar Odom
            'visual_odometry' : 'true', # Visual Odom
            'imu_topic' : '/rtabmap/imu',
            'wait_imu_to_init' : 'false',
            
            # LiDAR Arguments
            'subscribe_scan' : 'true',
            
            
            
            # Misc.
            'log_level' : 'debug', 
	        'approx_sync' : 'true',
            'qos' : '1',
	        'sync_queue_size' : '50',
	        'topic_queue_size' : '50',  
            'wait_for_transform' : '0.4',
	        'rtabmap_viz' : 'true',
            'map_topic' : '/map',
        }.items()
    )
    
    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[os.path.join(package_slam, 'config/ekf.yaml'), {'use_sim_time': 'true'}]
    )   
    

    return LaunchDescription([
        rtabmap,
        robot_localization_node
    ])
    
    