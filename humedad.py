import Adafruit_DHT

class HumiditySensor:
    def __init__(self, sensor, pin):
        self.sensor = sensor
        self.pin = pin

    def read_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity is not None:
            return round(humidity, 2)
        else:
            return None

# Ejemplo de uso
sensor = HumiditySensor(Adafruit_DHT.DHT11, 17)
humidity = sensor.read_humidity()

if humidity is not None:
    print('Humedad: {0}%'.format(humidity))
else:
    
    
    print('Error al leer la humedad del sensor.')
