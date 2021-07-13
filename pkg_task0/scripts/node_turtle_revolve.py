#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

def main():    
    
    # 1. Make the script a ROS Node.
    rospy.init_node('node_turtle_revolve', anonymous=True)
    
    # creating the velocity publisher
    cmd_vel_topic = '/turtle1/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist,queue_size=100)
    loop_rate = rospy.Rate(10)
    # defining the radius of the circle
    radius = 1.0
    # defining the velocity with which to move
    velocity = 1.0
    velocity_msg = Twist()
    velocity_msg.linear.x = velocity*radius
    velocity_msg.angular.z = velocity
    
    #theta = total angle traversed
    theta = 0.0
    time.sleep(1)
    startTime = rospy.Time.now().to_sec() 
    # moving till the angle covered is less than 2pi
    while theta < 2*math.pi:
        velocity_publisher.publish(velocity_msg)
        rospy.loginfo("Moving in a circle")
        print(theta*radius)
        theta = velocity*(rospy.Time.now().to_sec()-startTime)
        loop_rate.sleep()
    #stop the turtle once the circle is completed
    velocity_msg.linear.x = 0    
    velocity_msg.angular.z = 0
    velocity_publisher.publish(velocity_msg)
    rospy.loginfo("goal reached")
    rospy.spin()
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
