import cv2
import numpy as np
from matplotlib import pyplot as plt

data = cv2.CascadeClassifier("Resources//frontalFace.xml")
capture = cv2.VideoCapture(0)
dataa = []
while True:
    flag, img = capture.read()
    if flag:
        faces = data.detectMultiScale(img)
        for width, height, w, h in faces:
            cv2.rectangle(img, (width, height),(w+width, h+height), (0, 255, 0), 3)
        face = img[height:height+h, width:width+w]
        face = cv2.resize(face, (50, 50))
        print(len(dataa))
        if len(dataa) < 400:
            dataa.append(face)

    cv2.imshow('face Recong', img)
    if cv2.waitKey(1) == 27 or len(dataa)>= 200:
        break

capture.release()
cv2.destroyAllWindows()
np.save('with_Out_mask.npy',dataa)
plt.imshow(dataa[0])
