# pip3 install pygame==2.0.0.dev12
# pip3 install pyzbar
# pip3 install opencv-python
# sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0
# sudo apt-get install -y build-essential libzbar-dev
# pip3 install opencv-python
# sudo apt-get install libcblas-dev
# sudo apt-get install libhdf5-dev
# sudo apt-get install libhdf5-serial-dev
# sudo apt-get install libatlas-base-dev
# sudo apt-get install libjasper-dev
# sudo apt-get install libqtgui4
# sudo apt-get install libqt4-test


import pygame.camera as camera
import pygame.image as image
from PIL import Image
from pyzbar import pyzbar
import os, time

# os.system('sudo rmmod uvcvideo')
# time.sleep(2)
# os.system('sudo modprobe uvcvideo nodrop=1 timeout=5000 quirks=0x80')
# time.sleep(2)

camera.init()

cam_list = camera.list_cameras()

cam = camera.Camera(cam_list[0], (640, 480))
cam.start()
i = 0
#cam.stop()
while 1:
    i += 1
    time.sleep(1)
    cam.get_image()
    img = cam.get_image()
    img = image.tostring(img, "RGBA", False)
    img = Image.frombytes("RGBA", (640, 480), img)
    code = pyzbar.decode(img)
    print(i, code)
