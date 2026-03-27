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
            'odom_topic' : '/odom', # Filtered odometry from robot_localization
            'scan_topic' : '/scan', # LiDAR placeholder
            'map_topic' : '/map',
            
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
            'icp_odometry' : 'false', # Lidar Odom
            'visual_odometry' : 'false', # Visual Odom
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
	        #'rtabmap_viz' : 'true',
        }.items()
    )
    
    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[os.path.join(package_slam, 'config/ekf.yaml'), {'use_sim_time': 'true'}]
    )    
    
    # # Stereo odometry
    # stereo_odom_node = Node(
    #     package='rtabmap_odom', executable='stereo_odometry', name='stereo_odometry', output='screen',
    #     emulate_tty=True,
    #     parameters=[{
    #         'frame_id' : 'frame_id',
    #         'odom_frame_id' : 'vo_frame_id',
    #         'publish_tf' : 'publish_tf_odom',
    #         'ground_truth_frame_id' : 'ground_truth_frame_id',
    #         'ground_truth_base_frame_id' : 'ground_truth_base_frame_id',
    #         'wait_for_transform' : 'wait_for_transform',
    #         'wait_imu_to_init' : 'wait_imu_to_init',
    #         'always_check_imu_tf' : 'always_check_imu_tf',
    #         'approx_sync' : 'approx_sync',
    #         'approx_sync_max_interval' : 'approx_sync_max_interval',
    #         'config_path' : 'cfg',
    #         'topic_queue_size' : 'topic_queue_size',
    #         'sync_queue_size' : 'sync_queue_size',
    #         'qos' : 'qos_image',
    #         'qos_camera_info' : 'qos_camera_info',
    #         'qos_imu' : 'qos_imu',
    #         'subscribe_rgbd' : 'subscribe_rgbd',
    #         'guess_frame_id' : 'odom_guess_frame_id',
    #         'guess_min_translation' : 'odom_guess_min_translation',
    #         'guess_min_rotation' : 'odom_guess_min_rotation'}],
    #     remappings=[{            
    #         'left_image_topic_relay' : '/left/image_rect',
    #         'right_image_topic_relay' : '/right/image_rect',
    #         'left_camera_info_topic' : '/left/camera_info',
    #         'right_camera_info_topic' : '/right/camera_info',
    #         'rgbd_topic_relay' : '/rgbd_image',
    #         'odom_topic' : '/odom_stereo', # Hopefully changes where its publishing
    #         'imu_topic' : '/imu'}],
    #     arguments=['args', 'odom_args', "--ros-args", "--log-level", 'namespace', '.stereo_odometry:=', 'odom_log_level', "--log-level", 'stereo_odometry:=', 'odom_log_level'],
    #     prefix= 'launch_prefix',
    #     namespace= 'namespace'
    # ),

    # # ICP odometry
    # icp_odom_node = Node(
    #     package='rtabmap_odom', executable='icp_odometry', name="icp_odometry", output="screen",
    #     name='icp_odometry_node',
    #     emulate_tty=True,
    #     parameters=[{
    #         'frame_id' : 'frame_id',
    #         'odom_frame_id' : 'vo_frame_id',
    #         'publish_tf' : 'publish_tf_odom',
    #         'ground_truth_frame_id' : 'ground_truth_frame_id',
    #         'ground_truth_base_frame_id' : 'ground_truth_base_frame_id',
    #         'wait_for_transform' : 'wait_for_transform',
    #         'wait_imu_to_init' : 'wait_imu_to_init',
    #         'always_check_imu_tf' : 'always_check_imu_tf',
    #         'approx_sync' : 'approx_sync',
    #         'approx_sync_max_interval' : 'approx_sync_max_interval',
    #         'config_path' : 'cfg',
    #         'topic_queue_size' : 'topic_queue_size',
    #         'sync_queue_size' : 'sync_queue_size',
    #         'qos' : 'qos_image',
    #         'qos_camera_info' : 'qos_camera_info',
    #         'qos_imu' : 'qos_imu',
    #         'subscribe_rgbd' : 'subscribe_rgbd',
    #         'guess_frame_id' : 'odom_guess_frame_id',
    #         'guess_min_translation' : 'odom_guess_min_translation',
    #         'guess_min_rotation' : 'odom_guess_min_rotation'}],
    #     remappings=[{            
    #         'scan_topic' : '/scan',
    #         'scan_cloud_topic' : '/scan_cloud',
    #         'odom_topic' : '/odom_icp', # Hopefully changes where its publishing
    #         'imu_topic' : '/imu'}],
    #     arguments=['args', 'odom_args', "--ros-args", "--log-level", 'namespace', '.icp_odometry:=', 'odom_log_level'],
    #     prefix= 'launch_prefix',
    #     namespace= 'namespace'
    # ),   

    return LaunchDescription([
        #stereo_odom_node,
        #icp_odom_node,
        rtabmap,
        robot_localization_node
    ])
    
    