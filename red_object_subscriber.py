#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

def image_callback(ros_image):
  
#convert ros_image into an opencv-compatible image
  cv_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
  hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
  lower = (0,70,50)
  upper = (10,255,255)
  mask = cv2.inRange(hsv, lower, upper)
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
  for i in contours:

    area = cv2.contourArea(i)
    if area>100 and area<10000:
      x,y,w,h = cv2.boundingRect(i)
      cv2.rectangle(cv_image, (x,y), (x+w,y+h), (0,255,0), 2)
      cv2.imshow("Result", cv_image)
  cv2.waitKey(3)

if __name__ == '__main__':
    rospy.init_node('red_sub_node')
    image_sub = rospy.Subscriber("red_topic",Image, image_callback)
    rospy.spin()
    
