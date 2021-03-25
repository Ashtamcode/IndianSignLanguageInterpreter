"""
Test script to learn OpenCV
"""
import numpy as np
import cv2
import os

minValue = 70
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
capturing = False
timer = 0
char = ''

while True:
    # capture frame
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)
    
    # Coordinates of the ROI
    x1 = int(0.2*frame.shape[1])
    y1 = int(0.3*frame.shape[0])
    x2 = int(0.8*frame.shape[1])
    y2 = int(0.7*frame.shape[0])
    
    # draw a rect at ROI position
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255,0,0) ,1)

    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]

    # Filters
    grey = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(grey, (5, 5), 2)
    adaptThres = cv2.adaptiveThreshold(gauss, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    ret, thres = cv2.threshold(adaptThres, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    final = thres

    #cv2.putText(frame, 'henlo', (100, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 1)
    if capturing:
        timer += 0.5
        if timer >= 50:
            cv2.imwrite(char+'.jpg', final)
            capturing = False
            print('captured image')
        cv2.putText(frame, "Capturing for letter " + char + " in " + str(int(50-timer)//10) + "s", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
    
    cv2.imshow('input', frame)
    cv2.imshow('capture', final)

    if cv2.waitKey(1) & 0xFF == 27: # ESC key
        break
    if cv2.waitKey(1) & 0xFF == ord('a'):
        char = 'a'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('b'):
        char = 'b'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        char = 'c'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('d'):
        char = 'd'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('e'):
        char = 'e'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('f'):
        char = 'f'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('g'):
        char = 'g'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('h'):
        char = 'h'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('i'):
        char = 'i'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('j'):
        char = 'j'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('k'):
        char = 'k'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('l'):
        char = 'l'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('m'):
        char = 'm'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('n'):
        char = 'n'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('o'):
        char = 'o'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('p'):
        char = 'p'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        char = 'q'
        timer = 0
        capturing = True
        print('starting capture...')
    elif cv2.waitKey(1) & 0xFF == ord('r'):
        char = 'r'
        timer = 0
        capturing = True
        print('starting capture...')
    
    
cap.release()
cv2.destroyAllWindows()
