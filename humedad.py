import Adafruit_DHT

# set up sensor
sensor = Adafruit_DHT.DHT22
pin = 17

# read data from sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# trigger sensor
if humidity is not None and temperature is not None:
    dht22.trigger()
    print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
