#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool


class GpioEStop(Node):
    def __init__(self):
        super().__init__("gpio_estop")

        self.declare_parameter("use_sim_gpio", False)
        self.declare_parameter("sim_gpio_topic", "/sim_gpio_estop")

        self.declare_parameter("gpio_pin", 7)
        self.declare_parameter("gpio_mode", "BOARD")
        self.declare_parameter("active_high", True)
        self.declare_parameter("latch", True)
        self.declare_parameter("poll_hz", 50.0)
        self.declare_parameter("lock_topic", "/emergency_stop_lock")
        self.declare_parameter("reset_topic", "/emergency_stop_reset")

        self.use_sim_gpio = self.get_parameter("use_sim_gpio").value
        self.sim_gpio_topic = self.get_parameter("sim_gpio_topic").value

        self.pin = self.get_parameter("gpio_pin").value
        self.mode = self.get_parameter("gpio_mode").value.upper()
        self.active_high = self.get_parameter("active_high").value
        self.latch = self.get_parameter("latch").value
        self.poll_hz = float(self.get_parameter("poll_hz").value)
        self.lock_topic = self.get_parameter("lock_topic").value
        self.reset_topic = self.get_parameter("reset_topic").value

        self.estop_active = False
        self.last_published = None
        self.sim_gpio_high = False

        self.lock_pub = self.create_publisher(Bool, self.lock_topic, 10)

        self.reset_sub = self.create_subscription(
            Bool,
            self.reset_topic,
            self.reset_callback,
            10,
        )

        if self.use_sim_gpio:
            self.sim_sub = self.create_subscription(
                Bool,
                self.sim_gpio_topic,
                self.sim_gpio_callback,
                10,
            )
            self.GPIO = None
            self.get_logger().warn(
                f"Using sim GPIO topic: {self.sim_gpio_topic}"
            )
        else:
            import Jetson.GPIO as GPIO
            self.GPIO = GPIO

            GPIO.setmode(GPIO.BOARD if self.mode == "BOARD" else GPIO.BCM)
            GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

            self.get_logger().info(
                f"Using Jetson GPIO pin {self.pin}, mode {self.mode}"
            )

        self.timer = self.create_timer(1.0 / self.poll_hz, self.poll_gpio)
        self.publish_lock(False, force=True)

    def sim_gpio_callback(self, msg):
        self.sim_gpio_high = msg.data

    def gpio_requests_estop(self):
        if self.use_sim_gpio:
            high = self.sim_gpio_high
        else:
            high = self.GPIO.input(self.pin) == self.GPIO.HIGH

        return high if self.active_high else not high

    def poll_gpio(self):
        if self.gpio_requests_estop():
            self.estop_active = True
        elif not self.latch:
            self.estop_active = False

        self.publish_lock(self.estop_active)

    def reset_callback(self, msg):
        if not msg.data:
            return

        if self.gpio_requests_estop():
            self.get_logger().warn("Reset ignored: e-stop signal is still active.")
            self.estop_active = True
        else:
            self.get_logger().warn("E-stop latch reset.")
            self.estop_active = False

        self.publish_lock(self.estop_active, force=True)

    def publish_lock(self, locked, force=False):
        if not force and locked == self.last_published:
            return

        msg = Bool()
        msg.data = locked
        self.lock_pub.publish(msg)
        self.last_published = locked

        if locked:
            self.get_logger().error("E-STOP ACTIVE: twist_mux locked.")
        else:
            self.get_logger().info("E-stop clear: twist_mux unlocked.")

    def destroy_node(self):
        if not self.use_sim_gpio and self.GPIO is not None:
            self.GPIO.cleanup()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = GpioEStop()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()