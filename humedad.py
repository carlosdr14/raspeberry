import Adafruit_DHT
import time

class TemperatureSensor:
    def __init__(self, sensor, pin):
        self.sensor = sensor
        self.pin = pin

    def get_temperature_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if temperature is not None and humidity is not None:
            data = {'temperature': temperature, 'humidity': humidity}
            return data
        else:
            return None

class SensorMonitor:
    def __init__(self, sensor, pin):
        self.sensor = TemperatureSensor(sensor, pin)

    def monitor(self, duration):
        start_time = time.time()
        end_time = start_time + duration
        while time.time() < end_time:
            data = self.sensor.get_temperature_humidity()
            if data is not None:
                print("Temperature: {}C, Humidity: {}%".format(data['temperature'], data['humidity']))
            else:
                print("Failed to retrieve data.")
            time.sleep(1)

if __name__ == '__main__':
    sensor = Adafruit_DHT.DHT11
    pin = 17
    monitor = SensorMonitor(sensor, pin)
    monitor.monitor(10)
