import rclpy
from rclpy.node import Node
from std_msgs import msg
from enum import Enum, auto

class LedStatus(Enum):
    BLINKING = auto(),
    SOLID = auto()

def change_led_status(led_status: LedStatus):
    print("AAAH!")

class MyNode(Node):
    def __init__(self):
        # Initialize the node with a name
        super().__init__('led_bridge')
        
        # Enable LEDs
        change_led_status(LedStatus.SOLID)
        
        self.subscription = self.create_subscription(
            msg.Bool,
            '/enabled',
            self.listener_callback,
            10)
        
    def listener_callback(self, message):
        self.get_logger().info(f'Received: {message.data}')
        change_led_status(LedStatus.BLINKING)




def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
