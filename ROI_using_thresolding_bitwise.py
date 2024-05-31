#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 08:00:17 2024

@author: era
"""

"""
This Script consist funtionality of  Reason of interest using thresholding and bitwise operator
Taking specific object, spave from and object from compelte just remove  background

object image must be less in pixel size 

"""

import numpy as np 
import cv2 

#load two images 
img1 = cv2.imread("/home/era/Desktop/Work/Opencv_projects/Images/ironman.jpg")
img2 = cv2.imread("/home/era/Desktop/Work/Opencv_projects/Images/strom_breaker.JPG")

img1 = cv2.resize(img1, (1024, 650))
img2 = cv2.resize(img2, (400, 400)) 

#fix img2 into  img1

r,c,ch = img2.shape
print(r,c,ch)

# selecting roi 
# roi = img1[0:r,0:c]
roi = img1[0:r,0:c]

#converting into grayscale

img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#thresholding and creating mask

_,mask = cv2.threshold(img2_gray, 10 , 255, cv2.THRESH_BINARY)

# removing background using bitwise not operator
mask_inv = cv2.bitwise_not(mask)

# Putting mask into roi using bitwise and operator
img1_bg = cv2.bitwise_and(roi,roi, mask=mask_inv)

#take onluy rigion of figure from original 
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

#putting img in roi and modifying the main
res =cv2.add(img1_bg,img2_fg)

#final = img1

img1[0:r,0:c] = res

# Display the images
cv2.imshow("Original Image with Overlay", img1)
cv2.imshow("Object Image", img2)
cv2.imshow("Mask", mask)
cv2.imshow("ROI", roi)
cv2.imshow("Background without Object", img1_bg)
cv2.imshow("Isolated Object", img2_fg)
cv2.imshow("Combined Result", res)
cv2.waitKey(0)

cv2.destroyAllWindows()