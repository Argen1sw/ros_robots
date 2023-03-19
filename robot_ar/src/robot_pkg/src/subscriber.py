#!/usr/bin/env python3
import rospy
import motor_class
from std_msgs.msg import Int16

robot = motor_class.Robot(left_trim=0, right_trim=0)

def robot_nav(data):
    
    
    print("Direct:", data, " / ", "Sub Obj: ", data.data)

    #Basic Navigation logic that uses the listener input for navigate 
    if data.data == 1:
        
        robot.forward()
    elif data.data == 2:
        robot.backward()
    elif data.data == 3:
        robot.right()
    elif data.data == 4:
        robot.left()
    else:
        robot.stop()
        

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('input_subscriber', anonymous=True)

    rospy.Subscriber("user_output", Int16, robot_nav)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
