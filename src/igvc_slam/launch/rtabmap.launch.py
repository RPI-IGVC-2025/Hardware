from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

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
            'args': '--delete_db_on_start',
            'depth_topic': '/camera/camera/aligned_depth_to_color/image_raw',
            'rgb_topic': '/camera/camera/color/image_raw',
            'camera_info_topic': '/camera/camera/color/camera_info',
            'frame_id': 'base_link',
            'publish_tf_odom': 'true',
            'odom_topic': 'odom',
            'odom_frame_id': 'odom',
            'approx_sync': 'true',
            'rgbd_sync': 'true',
            'approx_rgbd_sync': 'true',
            'subscribe_rgbd': 'true',
            'visual_odometry': 'true',
            'qos': '1',
            'approx_sync_max_interval': '0.01',
            'sync_queue_size': '50',
            'topic_queue_size': '50',
            'wait_for_transform': '0.4',
            'imu_topic': '/rtabmap/imu',
            'wait_imu_to_init': 'true',
            'rtabmap_viz': 'true',
            'map_topic': '/map'
        }.items()
    )
    
    realsense = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('realsense2_camera'),
                'launch',
                'rs_launch.py'
            ])
        ),
        launch_arguments={
            'enable_color': 'true',
            'enable_depth': 'true',
            'align_depth.enable': 'true',
            'pointcloud.enable': 'false',
            'enable_sync': 'false',
            'unite_imu_method': '2',
            'enable_gyro': 'true',
            'enable_accel': 'true',
            'color_fps': '60',
            'depth_fps': '60',
            'gyro_fps': '200',
            'accel_fps': '63',
            'publish_tf': 'true'
        }.items()
    )
    
    imu_filter = Node(
        package='imu_filter_madgwick',
        executable='imu_filter_madgwick_node',
        output='screen',
        remappings=[
            ('/imu/data_raw', '/camera/camera/imu'),
            ('imu/data', '/rtabmap/imu')
        ],
        parameters=[
            {'use_mag': False},
            {'publish_tf': True},
            {'fixed_frame': 'camera_link'}
        ]
    )

    Nodes = [
        imu_filter,
        rtabmap,
        realsense
    ]

    return LaunchDescription(declared_arguments + Nodes)

