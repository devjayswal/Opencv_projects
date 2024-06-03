#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:45:10 2024

@author: era
"""

import numpy as np
import cv2

img = cv2.imread("/home/era/Desktop/Work/Opencv_projects/Images/col_balls.jpg")
img = cv2.resize(img, (600,600))
cv2.imshow("original", img)

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("canny")
cv2.createTrackbar("threshold", "canny", 0, 255, nothing)


while True:
    a = cv2.getTrackbarPos("threshold", "canny")
    print(a)
    res = cv2.Canny(img_g,a,255)
    cv2.imshow("canny", res)


cv2.waitKey(0)
cv2.destroyAllWindows()