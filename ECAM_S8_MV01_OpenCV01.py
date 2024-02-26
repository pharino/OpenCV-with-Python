#OpenCV could be install in terminal via: pip3 install python-opencv
import numpy as np #This is numpy package
import cv2 #This is mudule of OpenCV
import matplotlib as plt

img = cv2.imread('asset/img_sample_01.jpeg')
b, g, r = cv2.split(img)
img_matplot = cv2.merge([r,g,b])
cv2.imshow('An Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()