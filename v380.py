import cv2
import numpy as np

cap = cv2.VideoCapture("rtsp://admin:admin7@192.168.1.1/live/ch00_0")


while True:
	_, frame = cap.read()
	 
	cv2.imshow("Frame",frame)
	key = cv2.waitKey(1)

	if  key == 27:
		break

cap.release()
cv2.destroAllWindows()
