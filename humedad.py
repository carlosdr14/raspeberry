import Adafruit_DHT

# Configuración del sensor
sensor = Adafruit_DHT.DHT22
pin = 4

# Lectura de los valores de humedad y temperatura
humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

# Mostrar los valores de humedad y temperatura
if humedad is not None and temperatura is not None:
    print('Temperatura={0:0.1f}°C Humedad={1:0.1f}%'.format(temperatura, humedad))
else:
    print('Error al leer los valores. Intenta de nuevo!')

