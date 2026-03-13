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
	        'rtabmap_viz' : 'true',
        }.items()
    )
    
    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[os.path.join(package_slam, 'config/ekf.yaml'), {'use_sim_time': 'true'}]
    )    
    

    # Stereo odometry
    
    stereo_odom_node = Node(
        package='rtabmap_odom', executable='stereo_odometry', name="stereo_odometry", output="screen",
        emulate_tty=True,
        condition=IfCondition(PythonExpression(["'", LaunchConfiguration('icp_odometry'), "' != 'true' and '", LaunchConfiguration('visual_odometry'), "' == 'true' and '", LaunchConfiguration('stereo'), "' == 'true'"])),
        parameters=[{
            "frame_id": LaunchConfiguration('frame_id'),
            "odom_frame_id": LaunchConfiguration('vo_frame_id'),
            "publish_tf": LaunchConfiguration('publish_tf_odom'),
            "ground_truth_frame_id": LaunchConfiguration('ground_truth_frame_id').perform(context),
            "ground_truth_base_frame_id": LaunchConfiguration('ground_truth_base_frame_id').perform(context),
            "wait_for_transform": LaunchConfiguration('wait_for_transform'),
            "wait_imu_to_init": LaunchConfiguration('wait_imu_to_init'),
            "always_check_imu_tf": LaunchConfiguration('always_check_imu_tf'),
            "approx_sync": LaunchConfiguration('approx_sync'),
            "approx_sync_max_interval": LaunchConfiguration('approx_sync_max_interval'),
            "config_path": LaunchConfiguration('cfg').perform(context),
            "topic_queue_size": LaunchConfiguration('topic_queue_size'),
            "sync_queue_size": LaunchConfiguration('sync_queue_size'),
            "qos": LaunchConfiguration('qos_image'),
            "qos_camera_info": LaunchConfiguration('qos_camera_info'),
            "qos_imu": LaunchConfiguration('qos_imu'),
            "subscribe_rgbd": LaunchConfiguration('subscribe_rgbd'),
            "guess_frame_id": LaunchConfiguration('odom_guess_frame_id').perform(context),
            "guess_min_translation": LaunchConfiguration('odom_guess_min_translation'),
            "guess_min_rotation": LaunchConfiguration('odom_guess_min_rotation')}],
        remappings=[
            ("left/image_rect", LaunchConfiguration('left_image_topic_relay')),
            ("right/image_rect", LaunchConfiguration('right_image_topic_relay')),
            ("left/camera_info", LaunchConfiguration('left_camera_info_topic')),
            ("right/camera_info", LaunchConfiguration('right_camera_info_topic')),
            ("rgbd_image", LaunchConfiguration('rgbd_topic_relay')),
            ("odom", LaunchConfiguration('odom_topic')),
            ("imu", LaunchConfiguration('imu_topic'))],
        arguments=[LaunchConfiguration("args"), LaunchConfiguration("odom_args"), "--ros-args", "--log-level", [LaunchConfiguration('namespace'), '.stereo_odometry:=', LaunchConfiguration('odom_log_level')], "--log-level", ['stereo_odometry:=', LaunchConfiguration('odom_log_level')]],
        prefix=LaunchConfiguration('launch_prefix'),
        namespace=LaunchConfiguration('namespace')
    ),


    # ICP odometry
    icp_odom_node = Node(
        package='rtabmap_odom', executable='icp_odometry', name="icp_odometry", output="screen",
        emulate_tty=True,
        condition=IfCondition(LaunchConfiguration('icp_odometry')),
        parameters=[{
            "frame_id": LaunchConfiguration('frame_id'),
            "odom_frame_id": LaunchConfiguration('vo_frame_id'),
            "publish_tf": LaunchConfiguration('publish_tf_odom'),
            "ground_truth_frame_id": LaunchConfiguration('ground_truth_frame_id').perform(context),
            "ground_truth_base_frame_id": LaunchConfiguration('ground_truth_base_frame_id').perform(context),
            "wait_for_transform": LaunchConfiguration('wait_for_transform'),
            "wait_imu_to_init": LaunchConfiguration('wait_imu_to_init'),
            "always_check_imu_tf": LaunchConfiguration('always_check_imu_tf'),
            "approx_sync": LaunchConfiguration('approx_sync'),
            "config_path": LaunchConfiguration('cfg').perform(context),
            "topic_queue_size": LaunchConfiguration('topic_queue_size'),
            "sync_queue_size": LaunchConfiguration('sync_queue_size'),
            "qos": LaunchConfiguration('qos_image'),
            "qos_imu": LaunchConfiguration('qos_imu'),
            "guess_frame_id": LaunchConfiguration('odom_guess_frame_id').perform(context),
            "guess_min_translation": LaunchConfiguration('odom_guess_min_translation'),
            "guess_min_rotation": LaunchConfiguration('odom_guess_min_rotation')}],
        remappings=[
            ("scan", LaunchConfiguration('scan_topic')),
            ("scan_cloud", LaunchConfiguration('scan_cloud_topic')),
            ("odom", LaunchConfiguration('odom_topic')),
            ("imu", LaunchConfiguration('imu_topic'))],
        arguments=[LaunchConfiguration("args"), LaunchConfiguration("odom_args"), "--ros-args", "--log-level", [LaunchConfiguration('namespace'), '.icp_odometry:=', LaunchConfiguration('odom_log_level')], "--log-level", ['icp_odometry:=', LaunchConfiguration('odom_log_level')]],
        prefix=LaunchConfiguration('launch_prefix'),
        namespace=LaunchConfiguration('namespace')
    ),   

    return LaunchDescription([
        #stereo_odom_node,
        #icp_odom_node,
        rtabmap,
        robot_localization_node
    ])
    
    