import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class AutonomousArm(Node):
    def __init__(self):
        super().__init__('autonomous_arm')
        self.publisher_ = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        # Fixed the typo here:
        self.timer = self.create_timer(3.0, self.move_arm)
        self.pos = 1.0

    def move_arm(self):
        msg = JointTrajectory()
        msg.joint_names = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']

        point = JointTrajectoryPoint()
        # Safe trajectory: Gentle sway on the base and slight bend in the elbow
        point.positions = [self.pos, 0.5, 0.5, 0.0, 0.0, 0.0]
        point.time_from_start = Duration(sec=3, nanosec=0)

        msg.points = [point]
        self.publisher_.publish(msg)
        self.get_logger().info('Sending safe 6-DOF autonomous trajectory...')

        # Invert the base movement
        self.pos = -self.pos

def main(args=None):
    rclpy.init(args=args)
    node = AutonomousArm()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
