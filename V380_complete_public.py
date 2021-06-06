#!/usr/bin/env python

import requests
import cv2
import sys
from time import sleep
from pathlib import Path


public_ip = "192.168.2.110"
onvif_port = 8899  # 80
rtsp_url = "rtsp://admin:admin7@%s:554/live/ch00_0" % public_ip
ptz_url = "http://%s:%s/onvif/ptz" % (public_ip, onvif_port)
ptz_duration = 0.5  # sec

mydir = Path(__file__).parent

def read_file(f):
    with open(mydir / f) as xml:
        return xml.read()

# Set the name of the XML file.
xml_docs = {
    k: read_file(v) for k, v in [
        (105, "postup.xml"),  # i
        (44, "postdown.xml"),  # ,(comma)
        (106, "postleft.xml"),  # j
        (108, "postright.xml"),  # l
        (107, "poststop.xml"),  # k
    ]
}


def watch_camera() :
    cam = cv2.VideoCapture(rtsp_url)

    cv2.namedWindow("test")

    img_counter = 0

    headers = {'Content-Type':'text/xml'}
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1) % 256

        if k == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        elif k == 255:
            continue
        else:
            xml = xml_docs.get(k)
            if not xml:
                print(
                    "Invalid key:",
                    chr(k),
                    "\nPress one of (i/,/j/l/k/[SPACE]/[ESC])"
                    " for (up/down/left/right/stop/[write-png]/[exit]), respectively.",
                    file=sys.stderr
                )
                continue

            r = requests.post(ptz_url, data=xml)
            if k != 107:  # don't re-send stop
                sleep(ptz_duration)
                r = requests.post(ptz_url, data=xml_docs[107])

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    watch_camera()