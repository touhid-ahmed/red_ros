# red_ros
An object detection algorithm for red colored objects using color filtration method in openCV along with ROS.

1. The publisher node reads video from the webcam and publishes the frames on "red_topic"

2. The Subscriber node reads from the topic and applies color filtration technique along with contour detection to the frames and displays the output where any object in red is detected and a bounding rectangle is drawn around it.

![](result1.png)
![](result2.png)


Credits: Anis Koubaa

Link: https://www.youtube.com/watch?v=achgxjqOtiM&list=PLSzYQGCXRW1H8R2Bok_K8wcsE12_49alQ&index=13
