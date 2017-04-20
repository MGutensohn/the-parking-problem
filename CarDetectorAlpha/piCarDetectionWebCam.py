import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


pi_id = 0
spot_zero = 0
spot_zero_occupied = 0
spot_one = 1
spot_one_occupied = 0
spot_two = 2
spot_two_occupied = 0
spot_three = 3
spot_three_occupied = 0


cars_cascade = cv2.CascadeClassifier('anchor_cascade.xml')
# allow the camera to warmup
while(True):
    # Capture frame-by-frame
    ret, image = cap.read()


    cars = cars_cascade.detectMultiScale(image, scaleFactor = 1.03,
                                   minNeighbors = 0, minSize=(80,80))
    for (x, y, w, h) in cars:
        if x + w < 320:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_zero_occupied = 1
        else:
            spot_zero_occupied = 0
        if x >= 320 and x + w < 640:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_one_occupied = 1
        else:
            spot_one_occupied = 0
        if x >= 640 and x + w <= 960:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_two_occupied = 1
        else:
            spot_two_occupied = 0
        if x >= 960:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_three_occupied = 1
        else:
            spot_three_occupied = 0




    cv2.imshow('Video', image)


    # show the frame
    #cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF


    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
