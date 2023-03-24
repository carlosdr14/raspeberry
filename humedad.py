import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Configuración del pin GPIO
GPIO.setmode(GPIO.BCM)
DHT_PIN = 16 # El pin GPIO que se utiliza para el sensor DHT11

# Función para leer la temperatura y la humedad del sensor
def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None, None

# Bucle principal del programa
try:
    while True:
        temperature, humidity = read_sensor()
        if temperature is not None and humidity is not None:
            print('Temperatura={0:0.1f}°C  Humedad={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Error al leer el sensor.')
        time.sleep(2)  # Esperar 2 segundos antes de volver a leer el sensor

# Detener el programa cuando se presiona Ctrl-C
except KeyboardInterrupt:
    print('Programa detenido por el usuario.')
finally:
    GPIO.cleanup()  # Liberar los recursos del pin GPIO
