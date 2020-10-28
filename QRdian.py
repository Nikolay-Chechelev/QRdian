import pygame
import pygame.camera
from pyzbar import pyzbar
from PIL import Image

w = 640
h = 480

pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0", (w, h))
cam.start()
cam.get_image()
cam.get_image()
image = cam.get_image()
cam.stop()

while 1:
    pass

window = pygame.display.set_mode((w, h), pygame.RESIZABLE)
window.blit(image, (0, 0))
pygame.display.update()
img = pygame.image.tostring(image, "RGBA", False)
code_image = Image.frombytes("RGBA", (w, h), img)

code = pyzbar.decode(code_image)
print(code)
