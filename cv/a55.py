
import cv2
import numpy as np

# Reading the input image 
img = cv2.imread('limbo.png', 0)


kernel = np.ones((4,4), np.uint8)# Taking a matrix of size 5 as the kernel
# The first parameter is the original image,
# kernel is the matrix with which image is  
# convolved and third parameter is the number  
# of iterations, which will determine how much  
# you want to erode/dilate a given image.  
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Input', img)#imshow() method is used to display an image in a window
#cv2.imshow('Erosion', img_erosion)
#cv2.imshow('Dilation', img_dilation)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)

cv2.waitKey(0) 
