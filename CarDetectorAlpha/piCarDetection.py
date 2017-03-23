# import the necessary packages
import io
from fractions import Fraction
from picamera.array import PiRGBArray
from picamera import PiCamera
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

cars_cascade = cv2.CascadeClassifier('lbp_cascade.xml')

time.sleep(0.1)

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



for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array

    cars = cars_cascade.detectMultiScale(image, scaleFactor = 1.03,
                                   minNeighbors = 0, minSize=(200,200))
    for (x, y, w, h) in cars:
        if x + w < spot_one_ROI:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_one_occupied = 1
        else:
            spot_one_occupied = 0
        if x >= spot_one_ROI and x + w < spot_two_ROI:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_two_occupied = 1
        else:
            spot_three_occupied = 0
        if x >= spot_two_ROI and x + w <= spot_three_ROI:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_three_occupied = 1
        else:
            spot_two_occupied = 0
        if x >= spot_three_ROI:
            cv2.rectangle(image, (x, y), (x + w, y + h), (1, 255, 1), 2)
            spot_four_occupied = 1
        else:
            spot_four_occupied = 0
        


    cv2.imshow('Video', image)
    spotData = [(spot_one,spot_one_occupied,pi_id),
                (spot_two,spot_two_occupied,pi_id),
                (spot_three,spot_three_occupied,pi_id),
                (spot_four,spot_four_occupied,pi_id)]
    insert_spot_data(spotData)


    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    time.sleep(294)

    if key == ord("q"):
        break
