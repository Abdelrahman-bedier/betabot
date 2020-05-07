#!/usr/bin/env python

from __future__ import division
import rospy
import math
import random
from geometry_msgs.msg import Twist, Point
from sensor_msgs.msg import LaserScan
import time





angle=1

def callback(msg):
    twist=Twist()
    if (msg.ranges[0]>2 and msg.ranges[10]>2 and msg.ranges[-10]>2 and msg.ranges[-20]>2 and msg.ranges[-25]>2) :
        print("no obstacle")
        print(msg.ranges[-25])
        twist.linear.x=0.2
        twist.angular.z=0
        publish_msg.publish(twist)
    else:
        print("obstacle")
        twist.linear.x=0
        twist.angular.z=angle
        publish_msg.publish(twist)

rospy.init_node('betabot_obstacles_avoider')

random_angle=random.uniform(0,2*3.14)
publish_msg=rospy.Publisher('cmd_vel' , Twist, queue_size=1)

angular_v=1.57/2
seconds_angular=int(random_angle/angular_v)
twist=Twist()
for i in range(10*seconds_angular):
        twist.linear.x=0
        twist.angular.z=angular_v
        publish_msg.publish(twist)
        time.sleep(0.10)

print(random_angle)

rospy.Subscriber('scan', LaserScan,callback)



rospy.spin()
