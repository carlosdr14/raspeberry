import Adafruit_DHT
import time

class SensorTH:
    def __init__(self, sensor, pin):
        self.sensor = sensor
        self.pin = pin
    
    def get_temperature_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return round(temperature, 1), round(humidity, 1)
        else:
            return None
    
    def monitor(self, interval):
        print("Monitoring temperature and humidity...")
        while True:
            data = self.get_temperature_humidity()
            if data is not None:
                temperature, humidity = data
                print("Temperature: {:.1f}°C, Humidity: {:.1f}%".format(temperature, humidity))
            else:
                print("Failed to retrieve data from sensor.")
            time.sleep(interval)

sensor = SensorTH(Adafruit_DHT.DHT11, 22)
sensor.monitor(5)
