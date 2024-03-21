#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from turtlesim.msg import Pose
from sensor_msgs.msg import LaserScan
import tf_transformations
import time


class TurtleNavigationNode(Node):
    
    def __init__(self):
        super().__init__("navigation")
        self.get_logger().info("our navigation has started")
        
        self.initial_pose_publisher = self.create_publisher(
            PoseWithCovarianceStamped, "/initialpose", 10)
        
        self.goal_pose_publisher = self.create_publisher(
            PoseStamped, "/goal_pose", 10)
        
        self._pose_listener = self.create_subscription(
            Odometry, "/odom", self.robot_controller, 10)
        
        ###################### [Initial Location] ########################
        initial_pose = PoseWithCovarianceStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.pose.pose.position.x = 0.0
        initial_pose.pose.pose.position.y = 0.0

        qq = tf_transformations.quaternion_from_euler(0, 0, 90)
        initial_pose.pose.pose.orientation.x = qq[0]
        initial_pose.pose.pose.orientation.y = qq[1]
        initial_pose.pose.pose.orientation.z = qq[2]
        initial_pose.pose.pose.orientation.w = qq[3]
        self.initial_pose_publisher.publish(initial_pose)
        #################################
        time.sleep(1)
        ###################### [Destination] ########################
        goal = PoseStamped()
        goal.header.frame_id = 'map'
        goal.pose.position.x = -1.0
        goal.pose.position.y = 0.0
        qq = tf_transformations.quaternion_from_euler(0,0,1.57)
        goal.pose.orientation.x = qq[0]
        goal.pose.orientation.y = qq[1]
        goal.pose.orientation.z = qq[2]
        goal.pose.orientation.w = qq[3]
        self.goal_pose_publisher.publish(goal)
        

    def robot_controller(self, scan : LaserScan):
        pass    
         


def main(args=None):
    rclpy.init(args=args)
    node = TurtleNavigationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()