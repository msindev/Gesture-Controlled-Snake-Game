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

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    center = None

    if(len(cnts)) > 0:
        c = max(cnts, key = cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)

        M = cv2.moments(c)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, center, 5, (0,255,255), -1)

        pts = appendleft(center)

        for i in range(1, len(pts)):
            if pts[i-1] is None or pts[i] is None:
                continue

        thickness = int(np.sqrt(buffer / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1) & 0xFF

        if(key == ord('q')):
            break
video_capture.release()
cv2.destroyAllWindows()
