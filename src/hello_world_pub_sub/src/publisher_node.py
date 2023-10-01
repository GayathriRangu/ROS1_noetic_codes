#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher_node():
    rospy.init_node('hello_world_publisher_node',anonymous=True)
    rate=rospy.Rate(1)
    count=0

    pub=rospy.Publisher('hello_world_topic',String,queue_size=10) #define the publisher, its topic-where it publishes- to the topic 'hello_world_topic'

    while not rospy.is_shutdown():  
        message="hello world {}".format(count)  #define the message to be printed- with count
        rospy.loginfo(message) #print it as log
        pub.publish(message) #oublish the message
        count+=1 #increment the count
        rate.sleep()

if __name__=='__main__':
    try:
        publisher_node() #call
    except rospy.ROSInterruptException:
        pass
