import cv2

img = cv2.imread("Resources/pratham.jpg")
print(img.shape)

imgResize = cv2.resize(img,(480,300)) # width come first then height
#cv2.imshow("Resize",imgResize)
#cv2.imshow("pratham",img)

imgCropped = img[0:600,200:1334] # In crop height come first then width
cv2.imshow("Crop",imgCropped)
cv2.waitKey(0)