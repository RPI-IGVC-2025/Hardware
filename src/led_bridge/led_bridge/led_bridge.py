import rclpy
from rclpy.node import Node
from std_msgs import msg
from enum import Enum, auto
import RPi.GPIO as GPIO


output_pin = 23 

class LedStatus(Enum):
    BLINKING = auto(),
    SOLID = auto()

def change_leds(on):
    GPIO.output(output_pin, on)

class MyNode(Node):
    def __init__(self):
        # Initialize the node with a name
        super().__init__('led_bridge')
        self.get_logger().info("led bridge started")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(output_pin, GPIO.OUT)
        self.led_activity = LedStatus.SOLID
        change_leds(True)
        self.subscription = self.create_subscription(
            msg.Bool,
            '/enabled',
            self.listener_callback,
            10)

        self.blink_on = True
        self.timer = self.create_timer(0.25, self.timer_callback)

    def timer_callback(self):
        if self.led_activity == LedStatus.BLINKING:
            change_leds(self.blink_on)
            self.blink_on = not self.blink_on

    def listener_callback(self, message):
        self.get_logger().info(f'Received: {message.data}')
        if not message.data:
            self.get_logger().info("Changing LED status to SOLID")
            self.led_activity = LedStatus.SOLID
            change_leds(True)
        else:
            self.get_logger().info("Changing LED status to BLINKING")
            self.led_activity = LedStatus.BLINKING
        

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    GPIO.cleanup()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
