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
