from launch_ros.actions import Node

lane_points_node = Node(
    package='your_package',
    executable='lane_points_node',
    name='lane_points_node',
    output='screen',
    parameters=[{
        'image_topic': '/zed/zed_node/rgb/image_rect_color',
        'cloud_topic': '/zed/zed_node/point_cloud/cloud_registered',
        'output_topic': '/lanes/points',
        'roi_top_fraction': 0.45,
        'min_value': 170,
        'max_saturation': 90,
        'pixel_stride': 4,
        'max_points': 3000,
        'min_depth_m': 0.4,
        'max_depth_m': 8.0,
    }]
)