import numpy as np
import cv2

img = np.ones((512,512,3),np.uint8)
# img[:] = 255,0,0

# for making line

cv2.line(img,(0,0),(720,1280),(0,255,0),2) # not getting line till last
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),5) # 1st width then height and now till last line get 
#for rectangle

cv2.rectangle(img,(0,0),(250,400),(0,0,255),3) # red color
# circle

cv2.circle(img,(250,50),30,(255,255,0),5) # light blue color

# for text in images

cv2.putText(img,"Pratham ",(300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),5) # light green


# 3 for thickness 3rd col is for colour
# first col is for starting point
# second for pixels

cv2.imshow("New", img)
cv2.waitKey(0)

