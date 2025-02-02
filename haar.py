# -*- coding: utf-8 -*-
"""
Created on Thu Sep 4 17:27:56 2020

@author: Vanika
"""
import numpy as np
import cv2 # library opencv we use 3.4 but still known as 2 : alsi logs
from datetime import datetime as dt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#vc=cv2.VideoCapture(r"C:\Users\Vanika\Pictures\Camera Roll\sample.mp4") # this captures the video with delta delay from the system 

vc=cv2.VideoCapture(0)
count = 0
fontScale = 2
color = (0, 0, 255) 
thickness = 10
gcount = 0
while True: #to keep reading the frames from camera
    ret,frame=vc.read() # read will read one by one frame and save to frame
    if ret == False:
        break
    
    img=frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w] #region of interest
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

    cv2.putText(img, str(count), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, fontScale, (0, 0, 255) , thickness, cv2.LINE_AA)
    
    cv2.putText(img, str(gcount), (200, 100), cv2.FONT_HERSHEY_SIMPLEX, fontScale, (0, 255,0) , thickness, cv2.LINE_AA)

    cv2.imwrite("temp.jpg",img) 
    cv2.imshow("window_name",img) # the image is shown in a window : with name window_nameqqqq
    q = cv2.waitKey(1)
    if q == ord('q'): 
        break

cv2.destroyAllWindows()
vc.release()