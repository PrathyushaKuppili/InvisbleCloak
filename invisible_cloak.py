import cv2
import numpy as np

cap=cv2.VideoCapture(0)
back=cv2.imread('./image.jpg') #Reads the image
while cap.isOpened():
    ret,frame=cap.read() #take each frame
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#converts bgr color to hsv color.HSV is a hue saturation value.Difference between hsv and bgr is bgr provides primary colors which is combined hsv provides combinatin of color where the humans can see the exact one i.e the intensity of color
        #cv2.imshow("hsv",hsv)
        orange=np.uint8([[[0,88,255]]]) #orange color of rgb
        hsv_orange=cv2.cvtColor(orange,cv2.COLOR_BGR2HSV) #get hsv color of orange
        print(hsv_orange)
        l_orange=np.array([0,100,100])
        u_orange=np.array([10,255,255])
        mask=cv2.inRange(hsv,l_orange,u_orange)
        #cv2.imshow("mask",mask)
        #all things in orange color
        part1=cv2.bitwise_and(back,back, mask=mask) #It replace with the background image
        #cv2.imshow("part1",part1)
        mask=cv2.bitwise_not(mask)
        #part is not things in orange color
        part2=cv2.bitwise_and(frame,frame,mask=mask)
        #cv2.imshow("mask",part2)
        cv2.imshow("cloak",part1 + part2)
        if cv2.waitKey(5) == ord('q'): #If user enters q it gets quit
            break
        #while running  the total one we get [10,255,255] ie.[b+10 255 255]
cap.release()
cv2.destroyAllWindows()