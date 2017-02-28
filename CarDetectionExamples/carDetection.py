import numpy as np
import cv2
import time


cars_cascade = cv2.CascadeClassifier('lbp_cascade.xml')


img = cv2.imread('pictures/garagepic/pos/pos2.jpg')
cars = cars_cascade.detectMultiScale(img,scaleFactor = 1.03,
                                   minNeighbors = 0, minSize=(200,200))
for (x,y,w,h) in cars:
    if x+w <= 670:
        cv2.rectangle(img,(x,y),(x+w,y+h),(1,255,1),2)
    if x >= 675 and x+w <= 1365:
        cv2.rectangle(img,(x,y),(x+w,y+h),(1,255,1),2)
    if x >= 1419 and x+w <= 2085:
        cv2.rectangle(img,(x,y),(x+w,y+h),(1,255,1),2)
    if x >= 2085:
        cv2.rectangle(img,(x,y),(x+w,y+h),(1,255,1),2)

    resized_image = cv2.resize(img, (960, 680))

    cv2.imshow('cars?', resized_image)
    print w
    print h

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break



if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()