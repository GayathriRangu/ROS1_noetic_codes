#!/usr/bin/env python3
import rospy
if __name__=='__main__':
    rospy.init_node("test_node")

    rospy.loginfo("hello from test node")
    rospy.logwarn("this is a warning ")
    rospy.logerr("this is error")

    rospy.sleep(1.0)
    rospy.loginfo("end of progam")
    