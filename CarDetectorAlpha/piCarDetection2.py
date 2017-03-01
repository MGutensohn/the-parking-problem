# import the necessary packages
import io
from picamera.array import PiRGBArray
import picamera
import time
import cv2

cars_cascade = cv2.CascadeClassifier('lbp_cascade.xml')

with picamera.PiCamera() as camera:
    stream = io.BytesIO()



# capture frames from the camera
    for frame in camera.capture_continuous(stream, format="bgr",):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
        image = frame.array

        cars = cars_cascade.detectMultiScale(image, scaleFactor = 1.03,
                                   minNeighbors = 0, minSize=(200,200))
        for (x, y, w, h) in cars:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 1, 1), 1)


        cv2.imshow('Video', image)


    # show the frame
    #cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
        stream.truncate()
        stream.seek(0)
        if process(stream):
            break

    # if the `q` key was pressed, break from the loop

