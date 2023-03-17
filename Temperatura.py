import Adafruit_DHT
Adafruit_DHT.platform = Adafruit_DHT.Raspberry_Pi_2


# Configura el pin GPIO que está conectado al pin DATA del sensor
sensor = Adafruit_DHT.DHT11
pin = 5

# Intenta leer la temperatura y humedad del sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Si se pudo leer la temperatura y humedad, imprime los valores
if humidity is not None and temperature is not None:
    print('Temperatura={0:0.1f}°C Humedad={1:0.1f}%'.format(temperature, humidity))
else:
    print('Error al leer el sensor')
