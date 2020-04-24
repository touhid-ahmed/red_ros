# red_ros
An object detection algorithm for red colored objects using color filtration method in openCV along with ROS.

1. The publisher node reads video from the webcam and publishes the frames on "red_topic"
2. The Subscriber node reads from the topic and applies color filtration technique along with contour detection to the frames and displays the output
