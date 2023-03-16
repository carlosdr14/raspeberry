import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 5

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin, retries=5, delay_seconds=2)

