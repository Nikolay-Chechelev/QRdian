# pip3 install pygame==2.0.0.dev12
# pip3 install pyzbar
# pip3 install opencv-python
# sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0
# sudo apt-get install -y build-essential libzbar-dev
import pygame.camera as camera
import pygame.image as image
from pyzbar import pyzbar
from PIL import Image
import time

import threading

w = 640
h = 480

camera.init()


def routine(*args):
    cam_list = camera.list_cameras()
    print(cam_list)
    cam = camera.Camera(cam_list[0], (w, h))
    print(1)
    cam.start()
    while 1:
        time.sleep(2)
        print(2)
        img = cam.get_image()
        print(4)
        img = image.tostring(img, "RGBA", False)
        print(5)
        code_image = Image.frombuffer("RGBA", (w, h), img)
        print(6)
        code = pyzbar.decode(code_image)
        print(code)



# x = threading.Thread(target=routine, args=(None,))
# x.start()
# while 1:
#     time.sleep(1)

routine('q')
