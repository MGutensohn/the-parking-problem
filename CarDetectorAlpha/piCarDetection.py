# import the necessary packages
import io
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
#http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 3
rawCapture = PiRGBArray(camera, size=(1920, 1080))

cars_cascade = cv2.CascadeClassifier('lbp_cascade.xml')
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
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
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
