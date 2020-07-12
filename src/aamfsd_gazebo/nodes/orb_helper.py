#!/usr/bin/env python
import time
import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image ,CompressedImage
from ackermann_msgs.msg import AckermannDriveStamped
from cv_bridge import CvBridge, CvBridgeError
import random
from datetime import datetime



import math

class ImageOverlay:
    def __init__(self):

        self.asteering_raw=0

        self.imgl = np.ones((700,1000,3),dtype=np.uint8)*128 # default black background
        self.imgr = np.ones((700,1000,3),dtype=np.uint8)*128 # default black background
        # update the image to the new image from camera feed
    def image_callback_r(self, data):
        imgr = CvBridge().compressed_imgmsg_to_cv2(data)

	
 	hsv = cv2.cvtColor(imgr, cv2.COLOR_BGR2HSV)
    
    	lower_red = np.array([30,150,50])
    	upper_red = np.array([255,255,180])
    
    	mask = cv2.inRange(hsv, lower_red, upper_red)
    	self.imgr = cv2.bitwise_and(imgr,imgr, mask= mask)

    	#cv2.imshow('frame',self.img)
    	#cv2.imshow('mask',mask)
    	#cv2.imshow('res',res)
    
    	#k = cv2.waitKey(5) & 0xFF

    def image_callback_l(self, data):
        imgl = CvBridge().compressed_imgmsg_to_cv2(data)
	
 	hsv = cv2.cvtColor(imgl, cv2.COLOR_BGR2HSV)
    
    	lower_red = np.array([30,150,50])
    	upper_red = np.array([255,255,180])
    
    	mask = cv2.inRange(hsv, lower_red, upper_red)
    	self.imgl = cv2.bitwise_and(imgl,imgl, mask= mask)



	
    def overlayl(self):
        img_out = self.imgl.copy()
        return img_out

    def overlayr(self):
        img_out = self.imgr.copy()
        return img_out

      #  self.publisher.publish(ack_cmd)
    def run(self):
        rospy.init_node("orb_helper")

        #self.publisher = rospy.Publisher('overlay/compressed', CompressedImage, queue_size=1)
        
        # Read in camera feed, change first arg to read a different camera
        self.camera_subscriberl = rospy.Subscriber('/camera/left/image_raw/compressed', CompressedImage, self.image_callback_l, queue_size=1)
        self.camera_subscriberr = rospy.Subscriber('/camera/right/image_raw/compressed', CompressedImage, self.image_callback_r, queue_size=1)
        #self.publisher_l = rospy.Publisher('/robot_control/command', AckermannDriveStamped, queue_size=10)
	self.publisherl = rospy.Publisher('orb_helper/l', Image, queue_size=1)
	self.publisherr = rospy.Publisher('orb_helper/r', Image, queue_size=1)
        rate = rospy.Rate(3)  # default 3 Hz

        print("Running camera overlay in overlay/compressed")

        while not rospy.is_shutdown():
            imgl = self.overlayl()
	    imgr = self.overlayr()
	    compressed_imgl = CvBridge().cv2_to_imgmsg(imgl)
            self.publisherl.publish(compressed_imgl)
	    compressed_imgr = CvBridge().cv2_to_imgmsg(imgr)
            self.publisherr.publish(compressed_imgr)



if __name__ == "__main__":
 

    img = ImageOverlay()
    img.run()




