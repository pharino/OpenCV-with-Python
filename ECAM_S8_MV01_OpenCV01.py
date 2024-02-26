#OpenCV could be install in terminal via: pip3 install python-opencv
import numpy as np #This is numpy package
import cv2 #This is mudule of OpenCV

img = cv2.imread('asset/img_sample_01.jpeg')

cv2.imshow('An Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()