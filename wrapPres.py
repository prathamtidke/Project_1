import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")
width,height = 250,350

pt1 = np.float32([[513,453],[1381,383],[699,1695],[1621,1545]])
pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pt1,pt2)
imgOut = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Cards",imgOut)
cv2.waitKey(0)