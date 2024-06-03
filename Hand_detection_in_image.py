#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:09:41 2024

@author: era
"""
"""
Hand detection in open_cv  in a particular image 

"""

import numpy as np 
import cv2 



def nothing(x):
    pass


img = cv2.imread("/home/era/Desktop/Work/Opencv_projects/Images/hand.jpg")
img = cv2.resize(img, (600,700))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("hand",cv2.WINDOW_NORMAL)
cv2.medianBlur(img1, 9)

ret,thresh = cv2.threshold(img1, 240, 255, cv2.THRESH_BINARY_INV)

#find counters
cnts,hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#Loops
for c in cnts:
    epsilon = 0.0001*cv2.arcLength(c, True)
    data = cv2.approxPolyDP(c, epsilon, True)
    hull = cv2.convexHull(data)
    
    
    
    cv2.drawContours(img, [c], -1, (50,50,50),2)
    cv2.drawContours(img, [hull], -1, (0,255,0),2)
    cv2.imshow("hand", img)
    cv2.imshow("mask",img1)
    cv2.imshow("thresh", thresh)
    

cv2.waitKey(0)
cv2.destroyAllWindows()