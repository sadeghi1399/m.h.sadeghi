import numpy as np
import cv2

cap = cv2.VideoCapture(0) #create a VideoCapture object

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    ch = cv2.waitKey(1)#The function waitKey() waits for a key event for a "delay"
    if  ch == ord('e'):
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()
