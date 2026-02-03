from launch import LaunchDescription

def generate_launch_description():
    # Declare args
    declared_arguments = []

    #TODO add use_mock_hardware to declared arguments?
    
    
    # Init args

    # Get URDF

    # Get nodes
    
    # TODO In the examples, the controller manager is not spawned until the joint state broadcaster is. Do we need to do this?
    nodes = []

    return LaunchDescription(declared_arguments + nodes)