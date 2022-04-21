import cv2
data = cv2.CascadeClassifier("Resources//frontalFace.xml")

while True:
    img = cv2.imread("Resources//pratham.jpg")
    faces = data.detectMultiScale(img)
    for width ,height ,w,h in faces:
        cv2.rectangle(img,(width,height),(width+w,height+h),(0,255,0),3)

    cv2.imshow("Pratham",img)
    if cv2.waitKey(0) == 27: # ascii value of escape is 27
        break
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
