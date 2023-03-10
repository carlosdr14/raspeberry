import Adafruit_DHT
import time

class TemperatureSensor:
    def __init__(self, sensor, pin):
        self.sensor = sensor
        self.pin = pin

    def get_temperature_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None and temperature is not None:
            return {'temperature': temperature, 'humidity': humidity}
        else:
            return None

    def monitor(self, interval):
        while True:
            data = self.get_temperature_humidity()
            if data is not None:
                print('Temperature: {0:0.1f} C  Humidity: {1:0.1f} %'.format(data['temperature'], data['humidity']))
            else:
                print('Failed to get reading. Try again!')
            time.sleep(interval)

if __name__ == '__main__':
    sensor = TemperatureSensor(Adafruit_DHT.DHT11, 17)

