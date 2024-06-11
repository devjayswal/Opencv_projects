#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:06:29 2024

@author: era
"""

"""
This file have funtionality of Image Analyzation using histogram uisng matplotlib and opencv

"""

import numpy as np 
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('/home/era/Desktop/Work/Opencv_projects/Images/beuty.jpeg')

"""
# for greyscale image
hist = cv2.calcHist([img], [0], None, [256], [0,256])

"""
#for colorful images
b,g,r = cv2.split(img)
cv2.imshow("img", img)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

plt.hist(b.ravel(), 256,[0,256])
plt.hist(g.ravel(), 256,[0,256])
plt.hist(r.ravel(), 256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()