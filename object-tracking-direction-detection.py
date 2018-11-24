'''This script can detect objects specified by the HSV color and also sense the
direction of their movement. Implemented using OpenCV.'''

import cv2
import imutils
import numpy as np
from collections import deque
import time

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

buffer = 32

pts = deque[buffer]
(dX, dY) = (0, 0)
direction = ''

video_capture = cv2.VideoCapture(0)

time.sleep(2)

while True:
    ret, frame = video_capture.read()
    frame = imutils.resize(frame, width = 600)
    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)
    hsv_converted_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_converted_frame, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2)

    _,cnts,_ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    center = None
