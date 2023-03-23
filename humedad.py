import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 5

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print(f'Temperature={temperature:.1f}*C Humidity={humidity:.1f}%')
    else:
        print('Failed to get reading. Try again!')
    time.sleep(1)
