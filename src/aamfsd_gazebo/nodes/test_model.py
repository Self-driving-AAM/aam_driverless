#!/usr/bin/env python
import time
import cv2
import numpy as np
import rospy
from sensor_msgs.msg import CompressedImage
from ackermann_msgs.msg import AckermannDriveStamped
from cv_bridge import CvBridge, CvBridgeError
import random
from datetime import datetime

import tensorflow as tf


import math
from ackermann_msgs.msg import AckermannDrive
from ackermann_msgs.msg import AckermannDriveStamped
from geometry_msgs.msg import Twist
class ImageOverlay:
    def __init__(self):
        self.i=0.0
	self.temp=""
	self.number=0
        self.asteering_raw=0
        self.max_steering = 1
        self.min_steering = -1
        self.epsilon_steering = math.radians(0.001)
        self.img = np.ones((700,1000,3),dtype=np.uint8)*128 # default black background
        # update the image to the new image from camera feed
    def image_callback(self, data):
        self.img = CvBridge().compressed_imgmsg_to_cv2(data)




    def overlay(self):
        img_out = self.img.copy()
        return img_out


    def call_back2(self,data):
                
        ack_cmd = AckermannDriveStamped()
        ack_cmd.header.stamp = rospy.Time.now()

        drive = AckermannDrive()
        drive.speed = data.linear.x
        drive.steering_angle = data.angular.z
        # impose limits on commanded angle
        # datetime object containing current date and time
        now = datetime.now()
        print(self.i)
        drive.steering_angle=self.i
        ack_cmd.drive = drive
        self.publisher.publish(ack_cmd)
    def run(self):
        rospy.init_node("get_img")

        #self.publisher = rospy.Publisher('overlay/compressed', CompressedImage, queue_size=1)
        
        # Read in camera feed, change first arg to read a different camera
        self.camera_subscriber = rospy.Subscriber('/camera/left/image_raw/compressed', CompressedImage, self.image_callback, queue_size=1)
        self.publisher = rospy.Publisher('/robot_control/command', AckermannDriveStamped, queue_size=10)
        self.s=rospy.Subscriber("/cmd_vel", Twist, self.call_back2)

        rate = rospy.Rate(3)  # default 3 Hz

        #print("Running camera overlay in overlay/compressed")
        graph = tf.Graph()
        with graph.as_default():
            with tf.Session(graph=graph) as sess:
                with tf.gfile.FastGFile('./model_tf.pb', 'rb') as model_file:
                    graph_def = tf.GraphDef()
                    graph_def.ParseFromString(model_file.read())
                # init
                # choose ROI
                roi_x = 66
                roi_y = 200
                input_var = tf.placeholder("float32", [1, roi_x, roi_y, 3])
                [output_image] = tf.import_graph_def(graph_def, input_map={'input_1:0': input_var},
                                                     return_elements=['output/Sigmoid:0'],
                                                     name='')
                while True:

                    startTime = time.time()
                    image = self.overlay()
                    # from 1 dim to 3
                    image = (np.reshape(image, (height, width, 3))).astype(float)
                    # resize - cv2. we don't need crop (did it before)
                    image_BGR = cv2.resize(image, (roi_y, roi_x))
                    # convert to RGB
                    image = image_BGR[..., ::-1]
                    # normalization
                    image /= 255.0
                    img = np.expand_dims(image, axis=0)
                    # inference
                    pred = sess.run(output_image, feed_dict={input_var: img})

                    steering_pred = 1*((       max(0, int(((((pred[0][0])-0.5)*2)+0.5)*255))        - 0) * (3- -3) / (255 - 0) + -3)
                    self.i=steering_pred



if __name__ == "__main__":
    width = 672
    height = 376
    max_steering=255
    # allocate memory
    bitspixel = 24
    # get data from camera and display
    lineinc = width * int((bitspixel + 7) / 8)
    # calculate fps
    i = 0
    sumi = 0
    fps_q = []

    # graph and session

    img = ImageOverlay()
    img.run()




