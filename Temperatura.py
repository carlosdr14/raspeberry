import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 5
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin, retries=10, delay_seconds=2)


# Si se pudo leer la temperatura y humedad, imprime los valores
if humidity is not None and temperature is not None:
    print('Temperatura={0:0.1f}°C Humedad={1:0.1f}%'.format(temperature, humidity))
else:
    print('Error al leer el sensor')
