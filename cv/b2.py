import cv2
import numpy as np


cap=cv2.VideoCapture('video.mp4')

ret,frame1=cap.read()#first frame
ret,frame2=cap.read()#second frame


while cap.isOpened():

    diff=cv2.absdiff(frame1,frame2) #absolute difference between two frames
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY) #convert to gray image
    median = cv2.medianBlur(gray, 5)
    cv2.imshow("original video",frame1)#imshow() method is used to display an image in a window
    cv2.imshow("moving objects", median)


    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break
    frame1=frame2
    ret,frame2=cap.read()



cv2.destroyAllWindows()
cap.release()

cv2.filetr2d