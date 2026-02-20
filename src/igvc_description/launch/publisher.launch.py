import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
  declared_arguments = []
  # Set the path to this package.
  igvc_description_package  = FindPackageShare(package='igvc_description').find('igvc_description')
  default_urdf = PathJoinSubstitution(
    [
      igvc_description_package,
      'urdf',
      'robot.urdf.xacro'
    ]
  )
  

  declared_arguments.append( 
      DeclareLaunchArgument(
          'urdf_model',
          default_value=default_urdf,
          description='Absolute path to robot urdf file'
      )
  )
  declared_arguments.append(
      DeclareLaunchArgument(
          'gui',
          default_value='False',
          description='Flag to enable joint_state_publisher_gui'
      )
  )         

  declared_arguments.append(
      DeclareLaunchArgument(
          'use_robot_state_pub',
          default_value='True',
          description='Whether to start the robot state publisher'
      )
  )
  declared_arguments.append(
      DeclareLaunchArgument(
          'use_sim_time',
          default_value='False',
          description='Use simulation (Gazebo) clock if true'
      )
  )

  urdf_model = LaunchConfiguration('urdf_model')
  gui = LaunchConfiguration('gui')
  use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
  use_sim_time = LaunchConfiguration('use_sim_time')


  joint_state_publisher_node = Node(
      package='joint_state_publisher',
      executable='joint_state_publisher',
      name='joint_state_publisher',
      condition=UnlessCondition(gui)
    )
  joint_state_publisher_gui_node = Node(
      package='joint_state_publisher_gui',
      executable='joint_state_publisher_gui',
      name='joint_state_publisher_gui',
      condition=IfCondition(gui)
    )
    
  robot_state_publisher_node = Node(
      package='robot_state_publisher',
      executable='robot_state_publisher',
      name='robot_state_publisher',
      parameters=[{'use_sim_time': use_sim_time,
      'robot_description': Command([
          'xacro ', urdf_model,
          'use_mock_hardware:=', LaunchConfiguration('use_mock_hardware')
        ]
        )
      }]
      )
  foxglove_bridge_node = Node(
      package='foxglove_bridge',
      executable='foxglove_bridge'
  )
  Nodes = [
      joint_state_publisher_node,
      joint_state_publisher_gui_node,
      robot_state_publisher_node,
      foxglove_bridge_node]

  return LaunchDescription(declared_arguments + Nodes)
"""
  # Set the path to the URDF file
  default_urdf_model_path = os.path.join(igvc_description_package , 'urdf/robot.urdf.xacro')

  # Launch configuration variables specific to simulation
  

  gui = LaunchConfiguration('gui')
  urdf_model = LaunchConfiguration('urdf_model')
  use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
  use_sim_time = LaunchConfiguration('use_sim_time')
  
  declare_urdf_model_path_cmd = DeclareLaunchArgument(
    name='urdf_model', 
    default_value=default_urdf_model_path, 
    description='Absolute path to robot urdf file')
    
  declare_use_joint_state_publisher_cmd = DeclareLaunchArgument(
    name='gui',
    default_value='False',
    description='Flag to enable joint_state_publisher_gui')
   
  declare_use_robot_state_pub_cmd = DeclareLaunchArgument(
    name='use_robot_state_pub',
    default_value='True',
    description='Whether to start the robot state publisher')
  
  declare_use_sim_time_cmd = DeclareLaunchArgument(
    name='use_sim_time',
    default_value='False',
    description='Use simulation (Gazebo) clock if true')
    
  start_joint_state_publisher_cmd = Node(
    condition=UnlessCondition(gui),
    package='joint_state_publisher',
    executable='joint_state_publisher',
    name='joint_state_publisher')
  
  start_joint_state_publisher_gui_node = Node(
    condition=IfCondition(gui),
    package='joint_state_publisher_gui',
    executable='joint_state_publisher_gui',
    name='joint_state_publisher_gui')
    
  start_robot_state_publisher_cmd = Node(
    condition=IfCondition(use_robot_state_pub),
    package='robot_state_publisher',
    executable='robot_state_publisher',
    parameters=[{'use_sim_time': use_sim_time, 
    'robot_description': Command(
      [
        'xacro ', urdf_model,
        ' use_mock_hardware:=', LaunchConfiguration('use_mock_hardware')
       ]
      ),
    }],
    )
    
  start_foxglove_bridge_cmd = Node(
    package='foxglove_bridge',
    executable='foxglove_bridge'
  )
    launch_description = LaunchDescription(
    [
        DeclareLaunchArgument(
            'use_mock_hardware',
            default_value='false',
            description='Run in Simulation'
        ),

    ]
  )


  # Declare the launch options
  launch_description.add_action(declare_urdf_model_path_cmd)
  launch_description.add_action(declare_use_joint_state_publisher_cmd)
  launch_description.add_action(declare_use_robot_state_pub_cmd)  
  launch_description.add_action(declare_use_sim_time_cmd)

  # Add any actions
  launch_description.add_action(start_foxglove_bridge_cmd)
  launch_description.add_action(start_joint_state_publisher_cmd)
  launch_description.add_action(start_joint_state_publisher_gui_node)
  launch_description.add_action(start_robot_state_publisher_cmd)

  return launch_description
"""
