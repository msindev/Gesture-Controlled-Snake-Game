''' This script detects a object of specified object colour from the webcam video feed.
Using OpenCV library for vision tasks and HSV color space for detecting object of given specific color.'''

#Import necessary modules
import cv2
import numpy as np
from collections import deque
import time

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

buffer = 50

pts = deque(maxlen = buffer)

video_capture = cv2.VideoCapture(0)

time.sleep(2)

while True:
    ret, frame = video_capture.read()
    frame = cv.flip(frame,1)
    blurred_frame = cv2.GaussianBlur(frame, (10,10), 0)
    hsv_converted_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_converted_frame, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2)

    cv2.imshow('Masked Output', mask)

    cnts = cv2.findContours(mask.copy())
