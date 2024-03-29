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
img_grayscale = cv2.imread(args["image"], 0) #read file as gray scale color
height, width = img_grayscale.shape
I_x = np.zeros((height, width))
I_y= np.zeros((height, width))
I = np.zeros((height, width))

for i in range(1,height ,1):
    I_x[i,:] = img_grayscale[i,:] - img_grayscale[i-1,:]

for i in range(1,width,1):
    I_y[:,i] = img_grayscale[:,i] - img_grayscale[:,i-1]

for i in range(1,height ,1):
    for j in range(1, width, 1):
        I[i,j] = np.sqrt(I_x[i,j]**2 + I_y[i,j]**2)

##stack images together as one image 
#img_Vstack1 = np.concatenate((img_grayscale, I), axis=0)
#img_Vstack2 = np.concatenate((I_x, I_y), axis=0)
#img_print = np.concatenate((img_Vstack1, img_Vstack2), axis=1)
##show image in a window
#cv2.imshow("Original Image, H filtered, V filtered, Edage Detection",img_print)
        
cv2.imshow("Original Image", img_grayscale)
cv2.imshow("Horizontal Filtered Image", I_x)
cv2.imshow("Vertical Filtered Image", I_y)
cv2.imshow("Edge Filtered Image", I)

#wait for a key stroke
cv2.waitKey(0)
#kills all open windows
cv2.destroyAllWindows()