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

#Define threshol value
threshold1 = 30
threshold2 = 220

#calculate edge detection
img_edge = cv2.Canny(img_gray, threshold1, threshold2)

#show result images
cv2.imshow("Original Image", img_gray)
cv2.imshow("Canny Edge Detection", img_edge)



#wait for a key stroke
cv2.waitKey(0)
#kills all open windows
cv2.destroyAllWindows()