import Adafruit_DHT
import time

# Configura el pin del sensor
sensor = Adafruit_DHT.DHT11
pin = 5

while True:
    # Lee la temperatura y humedad del sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Si se lee un valor válido, muestra la temperatura y humedad en la consola
    if humidity is not None and temperature is not None:
        print(f"Temperatura = {temperature:.1f}°C  Humedad = {humidity:.1f}%")
    else:
        print("Error al leer el sensor")

    # Espera 2 segundos antes de leer nuevamente el sensor
    time.sleep(2)
