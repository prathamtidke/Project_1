# In this it will access our laptop cam

import cv2

captureDevice = cv2.VideoCapture(0) #captureDevice = camera
captureDevice.set(3,640) # 3 for width
captureDevice.set(4,480) # 4 for height
captureDevice.set(10,50) # 10 for brightness 50 is brightness level


while True:
    ret,frame = captureDevice.read() 

    cv2.imshow('my frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captureDevice.release()
cv2.destroyAllWindows()