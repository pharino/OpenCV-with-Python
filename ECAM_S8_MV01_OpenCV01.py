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
img_color = cv2.imread(args["image"], 1) #read file as image color
img_grayscale = cv2.imread(args["image"], 0) #read file as gray scale color
img_unchanged = cv2.imread(args["image"], -1) #read file as it is. Do not change properties.
cv2.imshow('A Color Image', img_color)
cv2.imshow('A Gray Scale Image', img_grayscale)
cv2.imshow('A Unchanged Properties Image', img_unchanged)

#wait for a key stroke
cv2.waitKey(0)

#kills all open windows
cv2.destroyAllWindows()

#write grayscale image to "asset" folder
cv2.imwrite("asset/sample_01_grayscale.jpg",img_grayscale)