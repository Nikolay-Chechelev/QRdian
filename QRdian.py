import pygame
import pygame.camera
from pyzbar import pyzbar
from PIL import Image
import time
import threading

w = 640
h = 480

pygame.init()
pygame.camera.init()


def routine(*args):
    cam = pygame.camera.Camera("/dev/video0", (w, h))
    print(1)
    cam.start()
    while 1:
        print(2)
        image = cam.get_image()

        window = pygame.display.set_mode((w, h), pygame.RESIZABLE)
        window.blit(image, (0, 0))
        pygame.display.update()
        print(4)
        img = pygame.image.tostring(image, "RGBA", False)
        print(5)
        code_image = Image.frombytes("RGBA", (w, h), img)
        print(6)
        code = pyzbar.decode(code_image)
        print(code)
        time.sleep(0.5)

    print(3)
    cam.stop()


x = threading.Thread(target=routine, args=(None,))
x.start()
while 1:
    time.sleep(1)
