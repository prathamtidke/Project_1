import cv2
data = cv2.CascadeClassifier("Resources//frontalFace.xml")

captureDevice = cv2.VideoCapture(0) #captureDevice = camera
captureDevice.set(3,640) # 3 for width
captureDevice.set(4,480) # 4 for height
captureDevice.set(10,50) # 10 for brightness 50 is brightness level


while True:
    flag,img = captureDevice.read()
    if flag:
        faces = data.detectMultiScale(img)
        for width,height,w,h in faces:
            cv2.rectangle(img,(width,height),(w+width,h+height),(0,255,0),3)
            
    cv2.imshow('face Recong', img)
    if cv2.waitKey(1) == 27:
        break

captureDevice.release()
cv2.destroyAllWindows()




# capture = cv2.VideoCapture(1)
# #capture.set(10,70)
# while True:
#     flag,img = capture.read()
#     if flag:
#         faces = data.detectMultiScale(img)
#         for width ,height ,w,h in faces:
#             cv2.rectangle(img,(width,height),(width+w,height+h),(0,255,0),3)

#     cv2.imshow("Pratham",img)
#     if cv2.waitKey(0) == 27: # ascii value of escape is 27
#         break


# capture.release()
# cv2.destroyAllWindows()
