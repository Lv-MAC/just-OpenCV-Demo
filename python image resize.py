import cv2
import imutils
img = cv2.imread("C:/Users/Administrator/Pictures/Untitled-1.png") #read an image
resizeImg = imutils.resize(img,width=100) #resize an image
cv2.imwrite("resizedImage1.png",resizeImg) #save an image
