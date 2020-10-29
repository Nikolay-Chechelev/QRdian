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

import cv2

cam = cv2.VideoCapture(1)
s, code_image = cam.read()
# detector = cv2.QRCodeDetector()
# data = detector.detectAndDecode(code_image)
# print(data)
cam.release()

