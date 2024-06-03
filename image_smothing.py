#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 08:17:48 2024

@author: era
"""

"""This file consist  5 methods of image smotthing or image buring.
Image smoothing and image buring  is most common  used operation  in Image Processing .
It is used to remove noise from the images


cv2.filter
"""

import cv2
import numpy as np

img = cv2.imread("Images/noisy.jpg")

cv2.imshow('orignal',img)

"""
Homogenous filter
this filter work like each output pixel  is the mean of its kernal 
neighbour 

kernal = kernal(5,5) /(25)

"""
kernel = np.ones((5,5),np.float32)/25
n_filter = cv2.filter2D(img,-1,kernel)
cv2.imshow("homogenous filter", n_filter)

"""
Blur filter
blur or average 
takes the average  of all the pixels order kernal area and replave the ventral 
elemesnt with the average
"""
blur = cv2.blur(img,(8,8))
cv2.imshow("blur filter ",blur)

" it is  special type of blur which used mathematical  formula"
gau = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow("gau", gau)

midfil = cv2.medianBlur(img, 5)
cv2.imshow("median filter", midfil)

"""
bileteral filter 
 it is highly effective at noise removial while  preserving edges
 it workd like garussian fikter but move focas  on edges  it is slow as compare with 
 other filter 
 Argument (img, neighbouer_pixel_diameter,sigma_Color, sigma_space)
 
"""
bif = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("bilateral filter", bif)

cv2.waitKey(0)
cv2.destroyAllWindows()