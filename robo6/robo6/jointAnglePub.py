#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from sensor_msgs.msg import JointState
from interface.msg import JointAngle

class AngleProcess(Node):
    def __init__(self,name):
        super().__init__(name)
        self.joint_sub = self.create_subscription(JointState, 'joint_states', self.sub_callback, 10)
        self.command_publisher_ = self.create_publisher(JointAngle, "command", 10) 
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.J1 = 0
        self.J2 = 0
        self.J3 = 0
        self.J4 = 0
        self.J5 = 0
        self.J6 = 0

    def sub_callback(self, msg):
        # self.get_logger().info("I heard: %s" % msg.name)
        # self.get_logger().info("I heard: %s" % msg.position)
        self.setAngle(msg.position[0], msg.position[1], msg.position[2], msg.position[3], msg.position[4], msg.position[5])

    def setAngle(self, joint1, joint2, joint3, joint4, joint5, joint6):
        self.J1 = joint1
        self.J2 = joint2
        self.J3 = joint3
        self.J4 = joint4
        self.J5 = joint5
        self.J6 = joint6

    def timer_callback(self):
        msg = JointAngle()
        msg.joint1 = self.J3
        msg.joint2 = self.J1
        msg.joint3 = self.J2
        msg.joint4 = self.J4
        msg.joint5 = self.J5
        msg.joint6 = self.J6
        self.command_publisher_.publish(msg)
        self.get_logger().info(f'Joint1 Angle：{msg.joint1}')
        self.get_logger().info(f'Joint2 Angle：{msg.joint2}')
        self.get_logger().info(f'Joint3 Angle：{msg.joint3}')
        self.get_logger().info(f'Joint4 Angle：{msg.joint4}')
        self.get_logger().info(f'Joint5 Angle：{msg.joint5}')
        self.get_logger().info(f'Joint6 Angle：{msg.joint6}')

def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = AngleProcess("angle_process_node")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy
