import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:

    ret, face = cap.read()

    if not ret:
        print("Can't receive face (stream end?). Exiting ...")
        break

    
    haar_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

    faces_rect = haar_cascade.detectMultiScale(face, scaleFactor=1.1, minNeighbors=10)

    closed = 0

    if len(faces_rect) != 0:
        print(f'Number of faces found = {len(faces_rect)}')
    else:
            print('WAKE UP!')

    for(x,y,w,h) in faces_rect:
        cv.rectangle(face, (x,y),(x+w , y+h), (110,255,110))

    
    cv.imshow('face', face)

    #cv.rectangle(ret,(384,0),(510,128),(0,255,0),3)
    if cv.waitKey(1) == ord('e'):
        break




cap.release()
cv.destroyAllWindows()