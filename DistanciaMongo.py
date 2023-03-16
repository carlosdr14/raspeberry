import RPi.GPIO as GPIO
import time
import json
from pymongo import MongoClient
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
# Save data to JSON file
def save_to_json(data):
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
 
# Save data to MongoDB
def save_to_mongodb(data):
    client = MongoClient('localhost', 27017)
    db = client['distance_sensor']
    collection = db['distance']
    collection.insert_one(data)
 
try:
    while True:
        dist = distance()
        print ("Measured Distance = %.1f cm" % dist)
 
        # Save data to JSON file
        data = {'distance': dist , 'timestamp': time.time()}
        save_to_json(data)
 
        # Save data to MongoDB
        save_to_mongodb(data)
 
        time.sleep(2)
 
# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
