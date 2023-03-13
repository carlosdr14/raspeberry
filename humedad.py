#Libraries
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
DHT_PIN = 17
 
def read_sensor():
    # read sensor data
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
 
    return temperature, humidity
 
try:
     while True:
      temperature, humidity = read_sensor()
      print("Temperature = {:.1f}°C, Humidity = {:.1f}%".format(temperature, humidity))
      time.sleep(2)
 
# Reset by pressing CTRL + C
except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
