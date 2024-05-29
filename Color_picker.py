#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:35:00 2024

@author: era
"""

"""
This file have funtionality of  color picker you can pick any color  using trackbar 

"""
import cv2
import numpy as np 


img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow("Color Picker")

def cross(x):
    pass

# Creting switch 
s = "0:0ff\n:on"
cv2.createTrackbar("S", "Color Picker", 0, 1, cross)

cv2.createTrackbar("R", "Color Picker", 0, 255, cross)
cv2.createTrackbar("G", "Color Picker", 0, 255, cross)
cv2.createTrackbar("B", "Color Picker", 0, 255, cross)

while True:
    cv2.putText(img, "Pink", (150,256), cv2.FONT_HERSHEY_TRIPLEX, 4, (100,100,100))
    cv2.imshow("Color Picker", img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    S = cv2.getTrackbarPos("S", "Color Picker")
    R = cv2.getTrackbarPos("R", "Color Picker")
    G = cv2.getTrackbarPos("G", "Color Picker")
    B = cv2.getTrackbarPos("B", "Color Picker")
    if S == 0:
        img[:] = 0
    else:
        img[:] = [R,G,B]

cv2.destroyAllWindows()
    