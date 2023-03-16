import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 5

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin, platform=Adafruit_DHT.DHT11)
