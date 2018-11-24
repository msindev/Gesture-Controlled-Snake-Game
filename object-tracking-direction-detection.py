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
