# import the necessary packages
import io
from fractions import Fraction
from picamera.array import PiRGBArray
from picamera import PiCamera
import threading
import time
import cv2

import MySQLdb

res_y = 1088
res_x = 1920

spot_one_ROI = res_x // 4
spot_two_ROI = spot_one_ROI * 2
spot_three_ROI = spot_one_ROI * 3

camera = PiCamera()
camera.resolution = (res_x,res_y)
rawCapture = PiRGBArray(camera)

cars_cascade = cv2.CascadeClassifier('anchor_cascade.xml')

time.sleep(.3)

level = 'floor_one'
spot_one = 001
spot_one_occupied = 0
spot_two = 002
spot_two_occupied = 0
spot_three = 003
spot_three_occupied = 0
spot_four = 004
spot_four_occupied = 0
pi_id = 0001

def insert_spot_data(spotData):
	query = "INSERT INTO " + level + " (spot_id,spot_avail,pi_id) " \
            "VALUES(%s,%s,%s)" \
            "ON DUPLICATE KEY UPDATE " \
            "spot_avail = VALUES(spot_avail)"

	conn = MySQLdb.connect(host="192.168.43.186",port=3306,user="root",passwd="rollins",db="tarveltparking")
	cursor = conn.cursor()
	cursor.executemany(query, spotData)
	conn.commit()


	cursor.close()
	conn.close()

def detect_car(image_array, spot):
    cars = cars_cascade.detectMultiScale(image_array, scaleFactor=1.03,
                                         minNeighbors=0, minSize=(200, 200))
    print cars
    for (x, y, w, h) in cars:
        spot_occupied = 1
    else:
        spot_occupied = 0

    #spotData = [(spot, spot_occupied, pi_id)]
    #insert_spot_data(spotData)


def detect_cars(image_array):
    cars = cars_cascade.detectMultiScale(image_array, scaleFactor=1.05,
                                         minNeighbors=0, minSize=(200, 200))
    print cars
    for (x, y, w, h) in cars:

        if x + w < spot_one_ROI:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_one_occupied = 1
            print 'spot one'
        else:
            spot_one_occupied = 0
        if x >= spot_one_ROI and x + w < spot_two_ROI:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_two_occupied = 1
            print 'spot 2'
        else:
            spot_three_occupied = 0
        if x >= spot_two_ROI and x + w <= spot_three_ROI:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_three_occupied = 1
            print 'spot 3'
        else:
            spot_two_occupied = 0
        if x >= spot_three_ROI:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_four_occupied = 1
            print 'spot 4'
        else:
            spot_four_occupied = 0

    cv2.imshow('Video', image)
    spotData = [(spot_one, spot_one_occupied, pi_id),
               (spot_two, spot_two_occupied, pi_id),
               (spot_three, spot_three_occupied, pi_id),
               (spot_four, spot_four_occupied, pi_id)]
    insert_spot_data(spotData)



for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array
    spot_1 = image[0:0, spot_one_ROI:1080]
    spot_2 = image[spot_one_ROI:0, spot_two_ROI:1080]
    spot_3 = image[spot_two_ROI:0, spot_three_ROI:1080]
    spot_4 = image[spot_three_ROI:0, res_x:1080]

    detect_1 = threading.Thread(target=detect_car, args=(spot_1, spot_one))
    detect_2 = threading.Thread(target=detect_car, args=(spot_2, spot_two))
    detect_3 = threading.Thread(target=detect_car, args=(spot_3, spot_three))
    detect_4 = threading.Thread(target=detect_car, args=(spot_4, spot_four))

    detect_1.start()
    detect_2.start()
    detect_3.start()
    detect_4.start()


    key = cv2.waitKey(1) & 0xFF
    detect_1.join()
    detect_2.join()
    detect_3.join()
    detect_4.join()

    time.sleep(54)
    rawCapture.truncate(0)





    if key == ord("q"):
        break
