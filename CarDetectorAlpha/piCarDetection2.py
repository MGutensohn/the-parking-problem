# import the necessary packages
import numpy
import io
from picamera.array import PiRGBArray
import picamera
import time
import cv2

cars_cascade = cv2.CascadeClassifier('lbp_cascade.xml')
stream = io.BytesIO()

with picamera.PiCamera() as camera:
    camera.resolution = (1920, 1080)

    # capture frames from the camera
    for frame in camera.capture_continuous(stream, format="bgr"):

        buffer = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

        image = cv2.imdecode(buff, 1)

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

