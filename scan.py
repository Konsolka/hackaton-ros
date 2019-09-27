#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
	print("Scan at 0:")
	print(msg.ranges[0])
	print("\nScan at 90:")
	print(msg.ranges[90])
	print("\nScan at 180:")
	print(msg.ranges[180])
	print("\n")
rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
