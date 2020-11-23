"""
Test script to learn OpenCV
"""
import numpy as np
import cv2
import os

minValue = 50
cap = cv2.VideoCapture(0)
capturing = False
timer = 0

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(grey, (5, 5), 2)
    adaptThres = cv2.adaptiveThreshold(gauss, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, thres = cv2.threshold(adaptThres, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    final = thres

    #cv2.putText(frame, 'henlo', (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 1)
    if capturing:
        timer += 0.5
        if timer >= 50:
            cv2.imwrite('capture.jpg', final)
            capturing = False
            print('captured image')
        cv2.putText(final, str(int(50-timer)//10), (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
    
    cv2.imshow('frame', final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        timer = 0
        capturing = True
        print('starting capture...')
    
cap.release()
cv2.destroyAllWindows()
