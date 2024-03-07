import cv2
text=("AIEC")
img = cv2.imread("C:/Users/Administrator/Pictures/Untitled-1.png")
cv2.putText(img,text,(500,1045),cv2.FONT_HERSHEY_SIMPLEX,20,(255,0,0),3)
cv2.imwrite("textinimage.png",img)
