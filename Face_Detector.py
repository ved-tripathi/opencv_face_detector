import cv2 as cv
from random import randrange

#training the machine 
trained_face_data = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#calling the test photo
# img = cv.imread('heavy_test.jpg')
webcam = cv.VideoCapture(0)


while True:
    

    successful_frame_read, frame = webcam.read()

    gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_coordinates = trained_face_cascade.detectMultiScale(gray_img)

    for x,y,w,h in face_coordinates:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255, 0), 2)

    cv.imshow("recogniser", frame)
    cv.waitKey(1)

    if key == 81 or key ==113:
        break    ### to stop, press Q
    

# release
webcam.release()

#
# #holding the output
# cv.waitKey()
print("have a good day")
