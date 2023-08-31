import cv2 as cv
import numpy as np
cap = cv.VideoCapture('\\Users\\lawrence\\Documents\\coding\\opencvprojectirp\\Distracted Driving.mp4')


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
       print("Nope")
       break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(25) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
