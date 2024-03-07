import cv2
img = cv2.imread("C:/Users/Administrator/Pictures/Untitled-1.png")
cv2.rectangle(img,(2090,2090),(200+100,200+100),(0,255,0),2)
cv2.imwrite("drawrectangle.png",img)
