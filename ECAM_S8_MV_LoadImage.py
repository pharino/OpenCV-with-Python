from __future__ import print_function
import argparse
import cv2

#construct the arguments parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", 
                required=True,
                help = "Path to the image")
args = vars(ap.parse_args())

#get image from parsing arguments
img = cv2.imread(args["image"])
cv2.imshow('An Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()