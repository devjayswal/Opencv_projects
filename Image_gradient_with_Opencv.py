#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:23:49 2024

@author: era
"""
"""
Image Gradient with opencv

it is a directional change in the color or intenseity  in an image . It is most important
part  to find information from images 

1. Like finding edge within the image
2. There are various methods to find image gradient  
caplacian derivatives sobelx and sobely
image should be in grey scale


"""
import numpy as np
import cv2

img = cv2.imread("/home/era/Desktop/Work/Opencv_projects/Images/col_balls.jpg")

cv2.imshow("original", img)

img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grey", img_g)
lap = cv2.Laplacian(img_g,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("lap", lap)

#SOBEL
Sobelx = cv2.Sobel(img_g, cv2.CV_64F, 1,0,ksize=3)
Sobely = cv2.Sobel(img_g, cv2.CV_64F,0,1,ksize= 3)
SObel_combine = cv2.bitwise_or(Sobelx,Sobely)

cv2.imshow("Sobel combine",SObel_combine)


cv2.waitKey(0)
cv2.destroyAllWindows()