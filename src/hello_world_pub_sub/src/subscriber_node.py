#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data): #callback function will be calld whenevr the subscriber gets executed
    rospy.loginfo("Received: %s",data.data) #here, it just prints the count/strng recvd frm the pub at the topic

def subscriber_node():
    rospy.init_node('hello_world_subscriber_node',anonymous=True)
    rospy.Subscriber('hello_world_topic',String,callback) #define the subscriber. Listening to the 'hello _world _topic'
    rospy.spin()

if __name__=='__main__':
    try:
        subscriber_node()
    except rospy.ROSInterruptException:
        pass