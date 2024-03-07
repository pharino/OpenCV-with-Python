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
cv2.imshow('A Color Image', img_color)
cv2.imshow('A Gray Scale Image', img_grayscale)

#image properties
print("Colored image size {}.".format(img_color.shape))
#print out value of a pixel of color image
px_color = img_color[100,100]
print( "Values of B/G/R pixels {}.".format(px_color))

#grayscale image properties
print("Gray scale image size {}.".format(img_grayscale.shape))
#print out value of a pixel of color image
px_grayscale = img_grayscale[100,100]
print( "Pixel intensity {}.".format(px_grayscale))

#extract region of interest from image
img_roi = img_grayscale[280:380, 330:430]
cv2.imshow('Image ROI', img_roi)

#wait for a key stroke
cv2.waitKey(0)

#kills all open windows
cv2.destroyAllWindows()
