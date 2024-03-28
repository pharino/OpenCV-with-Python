from __future__ import print_function
import argparse
import cv2
import numpy as np

#construct the arguments parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", 
                required=True,
                help = "Path to the image")
args = vars(ap.parse_args())
img_gray = cv2.imread(args["image"], 0) #read file as gray scale color

#calculate sobelx and sobely
sobelx = cv2.Sobel(img_gray,cv2.CV_64F, 1,0, ksize=3)
sobely = cv2.Sobel(img_gray,cv2.CV_64F, 0,1, ksize=3)

#show result images
cv2.imshow("Original Image", img_gray)
cv2.imshow("Sobel X Edge Detection", sobelx)
cv2.imshow("Sobel Y Edge Detection", sobely)
cv2.imshow("Sobel X+Y Edge Detection", (sobelx + sobely)/2)


#wait for a key stroke
cv2.waitKey(0)
#kills all open windows
cv2.destroyAllWindows()