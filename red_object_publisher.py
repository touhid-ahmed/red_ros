#! /usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()

rospy.init_node("red_pub_node")
red_pub = rospy.Publisher("red_topic", Image, queue_size = 10)
rate = rospy.Rate(25)

videocap = cv2.VideoCapture(0)
while not rospy.is_shutdown():
    ret, frame = videocap.read()
    # frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    img = bridge.cv2_to_imgmsg(frame, "bgr8")
    red_pub.publish(img)
    rate.sleep()
    
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("Initial", frame)
    if cv2.waitKey(30) & 0XFF==ord('q'):
        break
videocap.release()
cv2.destroyAllWindows()

    

