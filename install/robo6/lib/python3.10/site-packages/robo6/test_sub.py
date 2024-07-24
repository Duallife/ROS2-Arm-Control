#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class NodeSubscribe(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s!" % name)
        self.command_sub = self.create_subscription(JointState, 'joint_states', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info("I heard: %s" % msg.name)
        self.get_logger().info("I heard: %s" % msg.position)

def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = NodeSubscribe("test_sub")  # 新建一个节点
    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    rclpy.shutdown() # 关闭rclpy
