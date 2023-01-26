# coding:utf-8
#!/usr/bin/python
	
# Extract images from a bag file.
	
#PKG = 'beginner_tutorials'
import roslib;   #roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
	
# Reading bag filename from command line or roslaunch parameter.
#import os
#import sys
	
index_path = 'indexes/'   #        rgb        
timestamp_path= 'timestamps/' #                 
	
class ImageCreator():
	def __init__(self):
		self.bridge = CvBridge()
		count = 0
		index = 0
		with rosbag.Bag('vig.bag', 'r') as bag:  #    bag  ；
			for topic,msg,t in bag.read_messages():
		#		if topic == "/exposure": #   topic；w
				if topic == "/device_0/sensor_1/Color_0/image/data":
					try:
						cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
					except CvBridgeError as e:
						print(e)
						
					timestr = "%.6f" %  msg.header.stamp.to_sec()
					#%.6f        6 ，          ；
					#image_name = timestr+ ".jpg" #    ：   .png
					index_name = "{0:03d}".format(index)  + ".jpg"
					timestamp_name = timestr+".jpg"
					cv2.imwrite(index_path + index_name, cv_image)  #  ；
					cv2.imwrite(timestamp_path+timestamp_name, cv_image)
					index += 1

				elif topic == "camera/depth_registered/image_raw": #   topic；
						try:
							cv_image = self.bridge.imgmsg_to_cv2(msg,"16UC1")
						except CvBridgeError as e:
							print (e)
						timestr = "%.6f" %  msg.header.stamp.to_sec()
						#%.6f        6 ，          ；
						image_name = timestr+ ".jpg" #    ：   .png
						cv2.imwrite(depth_path + image_name, cv_image)  #  ；
	
if __name__ == '__main__':
	#rospy.init_node(PKG)
	try:
		image_creator = ImageCreator()
	except rospy.ROSInterruptException:
		pass

