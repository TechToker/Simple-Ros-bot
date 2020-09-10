#!/usr/bin/env python

import rospy
import keyboard
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def talker():
    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher_python')

    rate = rospy.Rate(24) # 24 frame per second
    hello_str = JointState()

    hello_str.header = Header()
    hello_str.header.stamp = rospy.Time.now()
    hello_str.name = ['body_to_leg_fl', 'body_to_leg_fr', 'body_to_leg_cl', 'body_to_leg_cr', 'body_to_leg_rl', 'body_to_leg_rr', 'body_to_hand_1', 'body_to_hand_2', 'body_to_hand_3']
    hello_str.velocity = []
    hello_str.effort = []

    while not rospy.is_shutdown():
      hello_str.header.stamp = rospy.Time.now()

      # Value in range [-3.14; 3.14]
      animVal = -1 * (rospy.get_time() % 6.28 - 3.14)
      rospy.loginfo(animVal)
      hello_str.position = [animVal, animVal, animVal, animVal, animVal, animVal, 0, 0, abs(animVal/15)]
      pub.publish(hello_str)
      rate.sleep()

    #set default value at finish
    rospy.loginfo('Python script closing')
    hello_str.position = [0, 0, 0, 0]
    pub.publish(hello_str)

    rate = rospy.Rate(0.5)
    rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
