#!/usr/bin/env python3

# TOPICS:
# cmd_vel: publish to, used for setting robot velocities
# scan : subscribing, used for seeing what's around the robot
import rospy

# msg needed for /scan
from sensor_msgs.msg import LaserScan

# msgs needed for /cmd_vel
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3


class Person_Follower(object):
    """ this node will follow whatever it's closest to"""
    def __init__(self):
        # start rospy node
        rospy.init_node("person_follow")

        # declare our node as a subscriber to the scan topic and
        # set self.process_scan as the function to be used for callback
        rospy.Subscriber("/scan", LaserScan, self.process_scan)
        # get a publisher to the cmd_vel topic
        self.twist_pub = rospy.Publisher("/cmd_vel",Twist, queue_size =10)  
        # set the minimum distance between robot and the person the robot is following
        self.min_distance = 0.5

    def process_scan(self,data):
        # determine closest object in range by looking at scan data
        # from around the robot.
        # set angular velocity based on that information, and publish
        # to cmd_vel
        
        # set default minimum distance from robot
        min_value = float('inf')
        # min_index documents the angle that the object closest 
        # to the robot lies on. the default value is 0
        min_index = 0
        # loops through ranges to find the angle that the object that is
        # closest to the robot lies on
        for angle, dist in enumerate(data.ranges):
            # check that it isn't 0 (which just means unreadable input) and is smaller than
            # the current minimum distance value
            if dist != 0 and dist < min_value:
                # if the angle is greater than 180, subtract 360 from it to make it negative
                # such that it's a left turn
                if angle >= 180:
                    min_index = angle - 360
                else: 
                    min_index = angle
                # update minimum distance value
                min_value = dist
        
        # now the angle is the amount of error degrees that needs to be corrected by turning.
        # by multiplying by 0.01, this ensures that the greater the error degree, the faster the
        # robot will turn
        error = min_index * 0.01

        # if min_value hasn't been updated then the robot detects nothing to be followed
        # if the min_value is less than 0.5 than the robot simply needs to face the object but not move
        # any closer
        if min_value == float('inf'):
            print("nothing to follow")
            follow_cmd = Twist()
            follow_cmd.linear.x = 0
            follow_cmd.angular.z = 0
            self.twist_pub.publish(follow_cmd)
        if min_value <= 0.5:
            print("object too close")
            # setup the Twist message 
            follow_cmd = Twist()
            follow_cmd.linear.x = 0
            # have the robot turn to face the object
            follow_cmd.angular.z = error
            # publish the message
            self.twist_pub.publish(follow_cmd)
        else:
            print("following")
            # else, we want to turn to the object and move closer
            # setup the Twist message
            follow_cmd = Twist()
            # slowly move towards it
            # turn to face the object
            
            follow_cmd.angular.z = error
            # publish the message
            follow_cmd.linear.x = 0.5

            self.twist_pub.publish(follow_cmd)
    def run(self):
        # this runs the robot
        rospy.spin()
if __name__ == '__main__':
    # instantiate the ROS node and run it
    node = Person_Follower()
    node.run()

