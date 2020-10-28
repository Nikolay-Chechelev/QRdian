# pip3 install pygame==2.0.0.dev12
# pip3 install pyzbar
# pip3 install opencv-python
# sudo apt-get install git curl libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0
# sudo apt-get install -y build-essential libzbar-dev

import pygame.camera
from pyzbar import pyzbar
from PIL import Image
import time
import threading

w = 640
h = 480



def routine(*args):
    cam = pygame.camera.Camera("/dev/video0", (w, h))
    print(1)
    while 1:
        pygame.camera.init()
        cam.start()
        print(2)
        image = cam.get_image()
        print(4)
        img = pygame.image.tostring(image, "RGBA", False)
        print(5)
        code_image = Image.frombytes("RGBA", (w, h), img)
        print(6)
        code = pyzbar.decode(code_image)
        print(code)
        time.sleep(0.5)
        cam.stop()
        pygame.quit()



x = threading.Thread(target=routine, args=(None,))
x.start()
while 1:
    time.sleep(1)
