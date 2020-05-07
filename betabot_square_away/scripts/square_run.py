#!/usr/bin/env python

from __future__ import division
import rospy
import math
from geometry_msgs.msg import Twist, Point



rospy.init_node('betabot_square_away')

r=rospy.Rate(10)


publish_msg=rospy.Publisher('cmd_vel' , Twist, queue_size=1)

side_length=2
linear_v=0.2
angular_v=1.57/2
seconds_linear=int(side_length/linear_v)
seconds_angular=int((math.pi/2)/angular_v)
while True:
    twist=Twist()
    for i in range(10*seconds_linear):
        twist.linear.x=linear_v
        twist.angular.z=0
        publish_msg.publish(twist)
        r.sleep()

    for i in range(10*seconds_angular):
        twist.linear.x=0
        twist.angular.z=angular_v
        publish_msg.publish(twist)
        r.sleep()


