#!/usr/bin/env python3
# TOPICS:
#       cmd_vel: publish to, used for setting robot velocity


import rospy

#msg needed for /cmd_vel
from geometry_msgs.msg import Twist, Pose, Point

class Drive_Square():
    """ This node publishes ROS messages containing the 3D coordinates of a single point """

    def __init__(self):
        # initialize the ROS node
        rospy.init_node('drive_square')
        # setup publisher to the cmd_vel ROS topic
        self.publisher = rospy.Publisher(('/cmd_vel'), Twist, queue_size = 1)
        r = rospy.Rate(20)
    def run(self):
        # ensure the robot keeps driving in a square
        while not rospy.is_shutdown():
            # ensure the robot completes all four sides of a square
            for i in range(4):
                # set the Twist message we want to send for the moving forward part
                drive_cmd = Twist()
                drive_cmd.linear.x = 0.5
                drive_cmd.angular.z = 0
                # publish the message
                self.publisher.publish(drive_cmd)
                # allow this message to be executed for 3 seconds
                rospy.sleep(3)
                # set the Twist message we want to send for the turning part
                drive_cmd.linear.x = 0
                drive_cmd.angular.z = 1.5708
                # publish the message
                self.publisher.publish(drive_cmd)
                # allow this message to be executed for enough time that the robot needs
                # to complete the turn
                rospy.sleep(1.12)

if __name__ == '__main__':
    # instantiate the ROS node and run it
    node = Drive_Square()
    node.run()



    
