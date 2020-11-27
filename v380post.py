import requests
import getch
from time import sleep

# Set the name of the XML file.
xml_up = "postup.xml"
xml_down = "postdown.xml"
xml_left = "postleft.xml"
xml_right = "postright.xml"
xml_stop = "poststop.xml"

headers = {'Content-Type':'text/xml'}
while True:
	char = getch.getch()
	if (char == 'i'):
		with open(xml_up) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)
		sleep(0.5)
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)

	elif (char == ','):
		with open(xml_down) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)

		sleep(0.5)
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)

	elif (char == 'j'):
		with open(xml_left) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)

		sleep(0.5)
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)

	elif (char == 'l'):
		with open(xml_right) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)

		sleep(0.5)
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)

	elif (char == 'k'):
		with open(xml_stop) as xml:
    		# Give the object representing the XML file to requests.post.
    			r = requests.post('http://192.168.0.148:8899/onvif/ptz', data=xml)
	elif (char == 'q'):
		break
	else:
		print("Failed")



