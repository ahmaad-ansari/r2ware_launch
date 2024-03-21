import rclpy
from rclpy.node import Node
from rosgraph_msgs.msg import Clock
from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSReliabilityPolicy

class ClockPublisher(Node):
    def __init__(self):
        super().__init__('r2ware_launch_node')

        # Define QoS profile for Clock topic
        qos_profile = QoSProfile(
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1,
            reliability=QoSReliabilityPolicy.BEST_EFFORT
        )

        self.clock_publisher = self.create_publisher(Clock, '/clock', qos_profile)

        # Create a timer to publish clock data at 100 Hz
        self.timer = self.create_timer(0.01, self.publish_clock)  # 1 / 100 = 0.01

    def publish_clock(self):
        # Get the current simulation time
        current_time = self.get_clock().now().to_msg()

        # Create a Clock message and populate it with the current time
        clock_msg = Clock()
        clock_msg.clock = current_time

        # Publish the Clock message
        self.clock_publisher.publish(clock_msg)

        # Log the published clock time
        # self.get_logger().info('Publishing clock: %s' % current_time)

def main(args=None):
    rclpy.init(args=args)
    clock_publisher = ClockPublisher()
    rclpy.spin(clock_publisher)
    clock_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
