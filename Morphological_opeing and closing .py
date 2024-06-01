#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:53:37 2024

@author: era
"""

"""
------------Morphological Transformation----------
Morphological transformations are simple operations based on the image shape.
They need two inputs: 1. the original image 2. the kernel.

Two basic Morphological transformations are:
1. Opening
2. Closing
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread("Images/col_balls.jpg", 0)  # Corrected file path


# Thresholding the image to create a binary mask
_, mask = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)

# Define the kernel
kernel = np.ones((3, 3), np.uint8)

# Opening: erosion followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Closing: dilation followed by erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Displaying the images using OpenCV
cv2.imshow("Original Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)

# Plotting the images using matplotlib
titles = ["Original Image", "Mask", "Opening", "Closing"]
images = [img, mask, opening, closing]
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Optional additional morphological transformations
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Tophat", tophat)
cv2.imshow("Gradient", gradient)
cv2.imshow("Blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
