import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):  

    ret, frame = cap.read()
    mirror = True
    size = (800, 600)

    if mirror is True :
        frame = frame[:, ::-1]
    
    if size is not None and len(size) == 2 :
        frame = cv2.resize(frame, size)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) == 13 :
        break
    
cap.release()
cv2.destroyAllWindows()