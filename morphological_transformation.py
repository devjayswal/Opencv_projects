#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:52:30 2024

@author: era
"""

"""
Morphological transformation are some simple operations based on the 
image shape it is normally performed on binary images. 
It needs  two inputs 1. original iamges 2. kernal
two basic morphological transformation are 1. Erosion 2. Dilation


"""

import cv2
import numpy as np 


"""
Erosion 
It erodes  away  the boundaries of foreground object 

Kernal slides  thorugh all the image and all the pixel
from  the original image conside 1 only if kernal's pixel is 1

"""
img= cv2.imread('/home/era/Desktop/Work/Opencv_projects/Images/color_balls.jpg',0)

_,mask = cv2.threshold(img, 2, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)
e = cv2.erode(mask,kernel)

cv2.imshow("img",img) 
cv2.imshow("ker=",kernel)
cv2.imshow("mask==",mask)
cv2.imshow("erosion==",e)


"""
Dilation
It is just opposite of erosion.
Here, a pixel elepment is '1' if atleast one pixel under the kernel
is '1' so it inc. The white region  in the image or size of foreground
 obejct in.
Normally in case like noise  removal, erosion is followed by dilaion 
Becuase, erosion removes white noises, but it also shrinks our object.
"""
kernel = np.ones((3,3),np.uint8)
d = cv2.dilate(mask, kernel)
cv2.imshow("dilate==", d)



# ploting  plot using  matplotlib

from matplotlib import pyplot as plt
titles = ['img','mask','erosion','dilation']
images = [img,mask,e ,d]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
