#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist_stamped.hpp>

class CmdVelBridge : public rclcpp::Node
{
public:
  CmdVelBridge()
  : Node("cmd_vel_bridge")
  {
    using geometry_msgs::msg::TwistStamped;

    pub_ = this->create_publisher<TwistStamped>("/bot_drive_controller/cmd_vel", 10);
    sub_ = this->create_subscription<TwistStamped>(
      "/cmd_vel_nav", 10,
      [this](const TwistStamped::SharedPtr msg)
      {
        pub_->publish(*msg);
      });
  }

private:
  rclcpp::Subscription<geometry_msgs::msg::TwistStamped>::SharedPtr sub_;
  rclcpp::Publisher<geometry_msgs::msg::TwistStamped>::SharedPtr pub_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<CmdVelBridge>());
  rclcpp::shutdown();
  return 0;
}

