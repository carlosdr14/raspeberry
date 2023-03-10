import Adafruit_DHT
import time

class HumiditySensor:
    def __init__(self, pin=17):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin

    def get_humidity_temperature(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return humidity, temperature
        else:
            return 0, 0

    def monitor(self, duration):
        start_time = time.time()
        while (time.time() - start_time) < duration:
            humidity, temperature = self.get_humidity_temperature()
            print("Humidity: {:.1f}%, Temperature: {:.1f}°C".format(humidity, temperature))
            time.sleep(1)

sensor = HumiditySensor()
sensor.monitor(60)  # Mide la humedad y la temperatura durante 60 segundos
