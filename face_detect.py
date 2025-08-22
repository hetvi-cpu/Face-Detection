#FACE DETECTION Using python
import cv2 as cv
import time
#REAL-TIME CAPTURING AND IDENTIFYING FACES 
face_cascade=cv.CascadeClassifier("C:\\Users\\Hp\\Desktop\\Edureka Python\\haar_cascade.xml")   
video=cv.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame=video.read()
    print(check)
    print(frame)
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=5)
                   #identifiy face (img,scale down size of mimg,)
    print("type=",type(faces))
    print("faces=",faces)
    for x,y,w,h in faces:
        frame=cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)   
    cv.imshow('caputuring',frame)
    key=cv.waitKey(1) 
    if key==ord('q'):
        break
print(a)
video.release()
cv.destroyAllWindows()   

