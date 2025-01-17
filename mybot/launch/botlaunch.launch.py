from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node  # 导入Node

def generate_launch_description():
    # 包含 gazebo.launch.py 文件
    gazebo_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/gazebo.launch.py'])
    )

    # 包含 gazebo_moveit_rviz.launch.py 文件
    gazebo_moveit_rviz_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/gazebo_moveit_rviz.launch.py'])
    )

    joint_angle_pub_node = Node(
        package='robo6',
        executable='jointAnglePub',
        name='joint_angle_publisher',
    )

    return LaunchDescription([
        gazebo_launch_file,
        gazebo_moveit_rviz_launch_file,
        # joint_angle_pub_node
    ])