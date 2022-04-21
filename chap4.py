# GreyImg, BlurImg 

import cv2
import numpy as np 

img = cv2.imread("Resources/pratham.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # gray
imgBlur = cv2.GaussianBlur(imgGray,(11,11),0)  # blur
imgCanny = cv2.Canny(img,100,200) # edge

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Edge",imgCanny)
cv2.waitKey(0)
