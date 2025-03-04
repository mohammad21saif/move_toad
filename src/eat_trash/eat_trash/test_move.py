import rclpy
from rclpy.node import Node
from mavros_msgs.msg import State

class MavrosTestNode(Node):
    def __init__(self):
        super().__init__('mavros_test_node')
        # Subscriber to /mavros/state topic
        self.state_subscriber = self.create_subscription(
            State,
            '/mavros/state',
            self.state_callback,
            10
        )
        self.get_logger().info("MAVROS Test Node Initialized. Listening to /mavros/state...")

    def state_callback(self, msg):
        """
        Callback function for /mavros/state topic.
        Logs the connection status, arming state, and flight mode.
        """
        self.get_logger().info(f"Connected: {msg.connected}, Armed: {msg.armed}, Mode: {msg.mode}")

def main(args=None):
    rclpy.init(args=args)
    node = MavrosTestNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down MAVROS Test Node...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

