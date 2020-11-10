import cv2
cap = cv2.VideoCapture(0)  #calling to captre the video i.e webcam 
while cap.isOpened():
    ret,back = cap.read() #Reading the image of the webcam. back is nothing but what the camera is reading,ret is searching that it is succesful or not
    if ret:    #If the image is there then its true 
        cv2.imshow("image",back) #It shows the image 
        if cv2.waitKey(5) == ord('q'): #If user enters q it gets quit
            cv2.imwrite('image.jpg',back) #saving the image
            break
cap.release()
cv2.destroyAllWindows()