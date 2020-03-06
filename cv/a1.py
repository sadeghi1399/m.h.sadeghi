import cv2
import numpy as np

img1 = cv2.imread("1.jpg")#imread() method loads an image from the specified file
gray_img=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY )
font                   = cv2.FONT_HERSHEY_SIMPLEX#It denotes the font type
bottomLeftCornerOfText = (10,30)#It is the coordinates of the bottom-left corner of the text string in the image
fontScale              = 1 #Font scale factor that is multiplied by the font-specific base size
fontColor1              = (0,250,0)#It is the color of text string to be drawn
fontColor2             = (0,0,0)#It is the color of text string to be drawn
lineType               = 2#This is an optional parameter.It gives the type of the line to be used

cv2.putText(img1,'98205816',
    bottomLeftCornerOfText,
    font,
    fontScale,
    fontColor1,
    lineType)#putText() method is used to draw a text string on any image

cv2.putText(gray_img,'98205816',
    bottomLeftCornerOfText,
    font,
    fontScale,
    fontColor2,
    lineType)#putText() method is used to draw a text string on any image

path1 = r'C:/Users\mohammad_hosein/Desktop/HW1/colorImg_with_texture1.jpg' #path of
path2 = r'C:/Users\mohammad_hosein/Desktop/HW1/grayImg_with_texture1.jpg' #path of


while (True):
   cv2.imshow("img with texture",img1) #imshow() method is used to display an image in a window
   cv2.imshow("grayImg with texture", gray_img)
   k = cv2.waitKey(1) & 0xFF
   if k == ord('s'):
       cv2.imwrite(path1, img1)  # imwrite() method is used to save an image to any storage device
       cv2.imwrite(path2, gray_img)  # imwrite() method is used to save an image to any storage device
       break



img2 = cv2.imread("football.jpg")
start_point = (305, 460)# Start coordinate, here (5, 5) represents the top left corner of rectangle
end_point = (370 ,530)# Ending coordinate, here (220, 220) represents the bottom right corner of rectangle
color = (0,255,0)# Blue color in BGR
thickness = 2 # Line thickness of 2 px
image = cv2.rectangle(img2, start_point, end_point, color, thickness)# Using cv2.rectangle() method Draw a rectangle with blue line borders of thickness of 2 px


cv2.imshow('footballImage_with_recangle', image)# Displaying the image
cv2.waitKey(0)

path = r'C:/Users\mohammad_hosein/Desktop/HW1/footballImage_with_recangle.jpg' #specift path to save image
cv2.imwrite(path,image)
ball=img2[460:530, 305:370]#pixels including ball in football image
img2[455:525, 560:625] =ball
cv2.imshow('footballImage_with_recangle',img2)
cv2.waitKey(0)
path = r'C:/Users\mohammad_hosein/Desktop/HW1/footballImage_with_2ball.jpg'
cv2.imwrite(path,img2) #save image














