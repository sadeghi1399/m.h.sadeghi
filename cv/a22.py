import cv2
import numpy as np

def nothing(x):
    print(x)
cv2.namedWindow('image')#The function namedWindow creates a window that can be used as a placeholder for images and trackbars
cv2.createTrackbar('Rotation degree','image',0,360,nothing) #The function createTrackbar creates a trackbar (a slider or range control) with the specified name and range

img1 = cv2.imread("space.jpg")#imread() method loads an image from the specified file
rows,cols,ht=img1.shape# .shape is a tuple that gives you an indication of the number of dimensions in the array

while(True):
    degree= cv2.getTrackbarPos('Rotation degree', 'image')#Returns the trackbar position
    img1 = cv2.imread("space.jpg")

    matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), degree, 0.5)#this method gives transformation matrix of rotation
    #point1 is=(1,1)
    x=np.matrix('1;1;1')
    point2=np.matmul(matrix,x)
    new_img = cv2.warpAffine(img1, matrix, (cols,rows))
    img1=cv2.resize(img1,(0,0),None,0.5,0.5)
    new_img  = cv2.resize(new_img ,(0, 0), None, 0.5, 0.5)

    hor=np.hstack((img1,new_img))#hstack() function is used to stack the sequence of input arrays horizontally (i.e. column wise) to make a single array
    hor=cv2.line(hor,(1,1),(int(point2[0]/2+img1.shape[1]),int(point2[1]/2)),(0,0,255))#cv2.line() method is used to draw a line on any image.

    k=cv2.waitKey(1)&0xFF

    if k==27:
       break


    cv2.imshow('image',hor)#imshow() method is used to display an image in a window

cv2.destroyAllWindows()