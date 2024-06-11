#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:37:11 2024

@author: era
"""

"""
This file consists of functionality for hand detection in live video capturing 
using OpenCV, contours, and convex hull features.
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('http://192.0.0.4:8080/video')

def nothing(x):
    pass

cv2.namedWindow("Color Adjustment", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustment", (400, 400))
cv2.createTrackbar("Thresh", "Color Adjustment", 0, 255, nothing)

# Color Detection Tracks
cv2.createTrackbar("Lower_H", "Color Adjustment", 0, 255, nothing)
cv2.createTrackbar("Lower_S", "Color Adjustment", 0, 255, nothing)
cv2.createTrackbar("Lower_V", "Color Adjustment", 0, 255, nothing)
cv2.createTrackbar("Upper_H", "Color Adjustment", 255, 255, nothing)
cv2.createTrackbar("Upper_S", "Color Adjustment", 255, 255, nothing)
cv2.createTrackbar("Upper_V", "Color Adjustment", 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (400, 400))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Getting all values
    l_h = cv2.getTrackbarPos("Lower_H", "Color Adjustment")
    l_s = cv2.getTrackbarPos("Lower_S", "Color Adjustment")
    l_v = cv2.getTrackbarPos("Lower_V", "Color Adjustment")
    u_h = cv2.getTrackbarPos("Upper_H", "Color Adjustment")
    u_s = cv2.getTrackbarPos("Upper_S", "Color Adjustment")
    u_v = cv2.getTrackbarPos("Upper_V", "Color Adjustment")

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    filter_with_mask = cv2.bitwise_and(frame, frame, mask=mask)

    m_g = cv2.getTrackbarPos("Thresh", "Color Adjustment")
    ret, thresh = cv2.threshold(mask, m_g, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(thresh, None, iterations=2)

    # Find contours
    cnts, hier = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        epsilon = 0.01 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)

        hull = cv2.convexHull(approx)
        cv2.drawContours(frame, [c], -1, (50, 50, 150), 2)
        cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)

    cv2.imshow("Thresh", thresh)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filter", filter_with_mask)
    cv2.imshow("Result", frame)

    key = cv2.waitKey(60) & 0xFF
    if key == 27: 
        break

cap.release()
cv2.destroyAllWindows()
