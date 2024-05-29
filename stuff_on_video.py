#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:16:22 2024

@author: era
"""

"""
This file have functionality to put text and shapes on videos 
"""


import cv2 
import datetime
#Open The vidoe file
cap = cv2.VideoCapture("/home/era/Desktop/Work/Opencv_projects/Images/videos/donkey.mp4")

#get the print the priginal width and height of the video frames 
print("for width",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("for hight",cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        #resize the frame
        frame = cv2.resize(frame, (800,600))
        # define the frame 
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        #creating text vaule for the video  height ant wedth
        text = ' Width: ' + str(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) + ' Height: ' + str(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        #Putting text on video 
        frame = cv2.putText(frame, text, (10,20), font, 1, (0,120,0),1,cv2.LINE_AA)
        # creating text for video date and time 
        data_text = "Data: "+str(datetime.datetime.now())
        #puttting text on image 
        frame = cv2.putText(frame, data_text, (20,50), font, 1, (100,5,255),1,cv2.LINE_AA)
        text_me = " Dev Jayswal"
        frame = cv2.putText(frame, text_me, (30,80), font, 1, (100,5,255),1,cv2.LINE_AA)
        frame = cv2.circle(frame, (400,300), 10, (0,0,248),5)
        # showing file
        cv2.imshow('frame',frame)
        # breaking the loop and exit using esc key
        if cv2.waitKey(30) & 0xFF == 27:
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()