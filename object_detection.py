#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:28:55 2024
this project  use hsv value to filter out objects  

@author: era
"""

import cv2 
import numpy as np 

frame = cv2.imread("/home/era/Desktop/Work/Opencv_projects/Images/imagination.jpeg")
frame = cv2.resize(frame, (600,400))

def nothing(x):
    pass

cv2.namedWindow("Color Adjustments")

cv2.createTrackbar("Lower_H","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustments",0,255,nothing)

cv2.createTrackbar("Upper_H","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Upper_S","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Upper_V","Color Adjustments",0,255,nothing)

while True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustments")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustments")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustments")
    
    u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustments")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustments")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustments")
    
    lower_bound = np.array([l_h,l_s,l_v])
    upper_bound = np.array([u_h,u_s,u_v])
    
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    res = cv2.bitwise_and(frame, frame,mask=mask)
    
    cv2.imshow("orignal", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    
    key = cv2.waitKey(1)
    if key ==27:
        break

cv2.destroyAllWindows()