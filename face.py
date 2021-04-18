import cv2
from random import randrange
#loading some pretrained data on face frontals from opencv haar cascade
train_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")





video = cv2.VideoCapture("y2mate.com - Megamind 2010  Metro Man Returns Scene 910  Movieclips_360p.mp4")
while True:
    success , frame = video.read()
    #grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coordinates = train_face_data.detectMultiScale(frame)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, x + h), (randrange(256), randrange(256), randrange(256)), 5)
        cv2.imshow("vid" , frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.waitKey(0)


#choosing an image for detecting faces in
#img = cv2.imread('jk.jpeg')
#cv2.imshow("face",img)

#cv2.waitKey(0)

#must conver to grayscale to get details
#grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



#cv2.imshow("face",grayscaled_img)
#webcam = cv2.VideoCapture(0)
#webcam.set(3,640)
#webcam.set(4,480)
#webcam.set(10,100)

#while True:
    #success,frame =webcam.read()
    #grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # detet faces
    #face_coordinates = train_face_data.detectMultiScale(grayscaled_img)

    # print(face_coordinates)

    # drawing rectangle
    #for (x,y,w,h) in face_coordinates:

       # cv2.rectangle(frame,(x,y),(x+w,x+h),(randrange(256),randrange(256),randrange(256)),5)

    #cv2.imshow("video",frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break
#cv2.waitKey()
#webcam.release()

#detet faces
#face_coordinates = train_face_data.detectMultiScale(grayscaled_img)

#print(face_coordinates)

#drawing rectangle
#for (x,y,w,h) in face_coordinates:

    #cv2.rectangle(img,(x,y),(x+w,x+h),(randrange(128,256),randrange(128,256),randrange(256)),5)



#cv2.imshow("face",img)
#cv2.waitKey(0)

