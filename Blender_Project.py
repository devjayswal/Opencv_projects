#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 19:16:26 2024

@author: era
"""

"""Blender is type of additon  of image where we add image 
        in specific way so that  we can combine it."""

import cv2
import numpy as np

img1 = cv2.imread("/home/era/Desktop/Work/Opencv_projects/Images/hero1.jpg")
img2 = cv2.imread("/home/era/Desktop/Work/Opencv_projects/Images/hero2.jpg")
img1 = cv2.resize(img1, (500,700))
img1 = cv2.flip(img1, 1)
img2 = cv2.resize(img2, (500,700))

cv2.imshow("Thor", img1)
cv2.imshow("Iron Man", img2)

def blend(x):
    pass


cv2.namedWindow("win")
switch = "0:OFF\n1:ON"
cv2.createTrackbar("switch", "win", 0, 1, blend)
cv2.createTrackbar("alpha", "win", 1, 100,blend)

while True:
    S = cv2.getTrackbarPos("switch", "win")
    a = cv2.getTrackbarPos("alpha", "win")
    if S==0:
        img = np.zeros((500,700,3),np.uint8)
    else:
        n = float(a/100)
        print(n)
        dst = cv2.addWeighted(img1, 1-n, img2, n, 0)
        cv2.putText(dst, str(a), (20,50), cv2.FONT_HERSHEY_COMPLEX, 2,(0,125,255),2)
        cv2.imshow("win", dst)
        
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
    

cv2.destroyAllWindows()