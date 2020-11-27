#!/usr/bin/env python

import requests
import getch
from time import sleep
import cv2

cam = cv2.VideoCapture("rtsp://admin:admin7@<public-ip>/live/ch00_0")

cv2.namedWindow("test")

img_counter = 0

# Set the name of the XML file.
xml_up = "postup.xml"
xml_down = "postdown.xml"
xml_left = "postleft.xml"
xml_right = "postright.xml"
xml_stop = "poststop.xml"

headers = {'Content-Type':'text/xml'}
while True:
	ret, frame = cam.read()
    	cv2.imshow("test", frame)
    	if not ret:
        	break
   	k = cv2.waitKey(1)

    	if k%256 == 27:
        	# ESC pressed
        	print("Escape hit, closing...")
        	break
    	elif k%256 == 32:
        	# SPACE pressed
        	img_name = "opencv_frame_{}.png".format(img_counter)
        	cv2.imwrite(img_name, frame)
        	print("{} written!".format(img_name))
        	img_counter += 1

	elif k%256 == 105:
		with open(xml_up) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)
		sleep(0.5)
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)

	elif k%256 == 44:
		with open(xml_down) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)

		sleep(0.5)
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)

	elif (k%256 == 106):
		with open(xml_left) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)

		sleep(0.5)
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)

	elif (k%256 == 108):
		with open(xml_right) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)

		sleep(0.5)
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)

	elif (k%256 == 107):
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://<public-ip>/onvif/ptz', data=xml)
	

cam.release()

cv2.destroyAllWindows()



