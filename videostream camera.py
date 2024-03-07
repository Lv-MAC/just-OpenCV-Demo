import cv2
vs = cv2.VideoCapture(0) #initialize the camera, 0 for default camera, put 1 if you have webcam
while True:
    ret,img = vs.read() #reading the frame from camera, while is used for infinite capturing
    cv2.imshow("VideoStream", img)
    key = cv2.waitKey(10) & 0xFF
    if key == ord("q"):
        break
vs.release() #releasing the camera
cv2.destroyAllWindows() #for closing all window
    
