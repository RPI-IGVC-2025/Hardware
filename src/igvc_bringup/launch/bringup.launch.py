from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_sim = LaunchConfiguration('use_sim')
    use_mock_hardware = LaunchConfiguration('use_mock_hardware')
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        # Launch Arguments
        DeclareLaunchArgument(
            'use_sim',
            default_value='false',
            description='Run in Simulation'
        ),
        DeclareLaunchArgument(
            'sim_world',
            default_value='empty_world',
            description='The name of the scenario to open in Gazebo'
        ),
        DeclareLaunchArgument(
            'use_mock_hardware',
            default_value=use_sim, # You are always mocking in simulation, but can specify if you need to bypass physical descriptors for testing
            description='Mocks all hardware'
        ),
        
        DeclareLaunchArgument(
            'use_slam',
            default_value='true', 
            description='Launch rtabmap for SLAM'
        ),
        
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation time'
       ),


        # Publishers & URDF
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_description'),
                 '/launch',
                 '/publisher.launch.py']
            ),
            launch_arguments={
                'use_mock_hardware': use_mock_hardware, 
                'use_sim_time' : use_sim_time, 
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
            launch_arguments={
                'use_sim_time' : use_sim_time, 
            }.items(),
        ),

        # ROS2_Control
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_hardware'),
                 '/launch',
                 '/control.launch.py']
            ),
            launch_arguments={
                'use_sim_time' : use_sim_time, 
            }.items(),
        ),

        # Real hardware
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_hardware'),
                 '/launch',
                 '/hardware.launch.py']
            ),
            condition = UnlessCondition(use_mock_hardware), 
            launch_arguments={
                'use_sim_time' : use_sim_time, 
            }.items(),
        ),

        # SLAM
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [FindPackageShare('igvc_slam'),
                 '/launch',
                 '/sim_rtabmap.launch.py']
            ),
            condition = IfCondition(LaunchConfiguration('use_slam')),
            launch_arguments={
                'use_sim_time' : use_sim_time, 
            }.items(),
        ),
        
        # TODO Nav
    ])
