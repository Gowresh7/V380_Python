# V380_Python

Python Codes for V380 cameras. The Python codes provide the following options:-

1. Live Streaming from Camera (Local and Remote)
2. PTZ Control of Camera (Local and Remote)
3. Image Capture

## Install

```
git clone --depth=1 https://github.com/Gowresh7/V380_Python V380_Python.git
python3 -m venv --prompt V380 V380.venv
. V380.venv/bin/activate 
pip install opencv-contrib-python
```

## Usage on local network:

1. Setup the V380 camera.
2. Find the wireless network of the camera and connect your system to it.
3. Find the IP address of the camera ( generally 192.168.1.1 for wireless)
4. Replace the ip-address in the python files
   (rtsp://<username>:<password>@<ip-address>/live/ch00_0, http://<ip-address>:8899/onvif/ptz)
   If no username or password, just enter the ip-address alone.
5. `PYTHONPATH=./V380_Python.git  python -m V380_complete_public`

## Usage remotely:

1. Connect the camera with ethernet.
2. Find the ip address assigned to camera
3. Do port-forward settings in router to map the ip to specific ports. Generally rtsp uses 554 and onvif ptz uses 8899 ports
4. Change the ip address in V380_complete_public.py
   (For rtsp url change as rtsp://username:password@,public_ip>/live/ch00_0,
   for ptz http://<public-ip>/onvif/ptz, forwarded port should contain the port)
5. `PYTHONPATH=./V380_Python.git  python -m V380_complete_public`


## Usage

Press the followimg keys:-

i - up
, - down
j - left
l - right
k - stop

## Files

(other files than `V380_complete_public` may need some fixes)

- v380.py - Live Stream of V380
- v380cap.py - Live Stream with Image Capture of V380 (Press SPACE to capture image)
- v380post.py - ptz control of V380
- V380_complete.py - Live Stream, Image Capture, PTZ control
- V380_complete_public.py - Same as V380_complete.py with Public ip.
