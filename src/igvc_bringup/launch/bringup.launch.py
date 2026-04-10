from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    declared_arguments = []
    
    declared_arguments.append(
        DeclareLaunchArgument(
            'use_sim',
            default_value='false',
            description='Run in Simulation'
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'sim_world',
            default_value='track_v1',
            description='The name of the scenario to open in Gazebo'
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'use_mock_hardware',
            default_value=LaunchConfiguration('use_sim'),
            description='Mocks all hardware'
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'use_slam',
            default_value='true',
            description='Launch rtabmap for SLAM'
        )
    )
    
    use_sim = LaunchConfiguration('use_sim')
    sim_world = LaunchConfiguration('sim_world')
    use_mock_hardware = LaunchConfiguration('use_mock_hardware')
    use_slam = LaunchConfiguration('use_slam')
   
    publisher_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('igvc_description'),
            '/launch',
            '/publisher.launch.py'
        ]),
        launch_arguments={
            'use_mock_hardware': use_mock_hardware
        }.items()
    )
    
    sim_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('igvc_gazebo'),
            '/launch/',
            sim_world,
            '.launch.py'
        ]),
        condition=IfCondition(use_sim)
    )

    control_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare('igvc_hardware'),
            '/launch/control.launch.py'
        ])
    )
    
    
    return LaunchDescription([
        # Publishers & URDF
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_description'),
                 '/launch',
                 '/publisher.launch.py']
            ),
            launch_arguments={
                'use_mock_hardware': use_mock_hardware
                }.items()
        ),

        # Simulation
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_gazebo'),
                 '/launch/',
                 LaunchConfiguration('sim_world'),
                 '.launch.py'
                ]
            ),
            condition=IfCondition(use_sim),
        ),

        # ROS2_Control
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_hardware'),
                 '/launch',
                 '/control.launch.py']
            ),
        ),

        # Real hardware
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_hardware'),
                 '/launch',
                 '/hardware.launch.py']
            ),
            condition = UnlessCondition(use_mock_hardware)
        ),

        # SLAM
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_slam'),
                 '/launch',
                 '/sim_rtabmap.launch.py']
            ),
            condition = IfCondition(LaunchConfiguration('use_slam'))
        ),
        
        # TODO Nav
    ])
