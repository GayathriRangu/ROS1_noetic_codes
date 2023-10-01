#!/usr/bin/env python3
import rospy
if __name__=='__main__':
    rospy.init_node("test node")
    rospy.loginfo("Test node has been started")

    rate=rospy.Rate()