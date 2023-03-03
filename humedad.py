import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configurar el pin de lectura del sensor de humedad
hum_pin = 17
GPIO.setup(hum_pin, GPIO.IN)

# Función para leer la humedad del suelo
def read_humidity():
    hum = 0
    for i in range(10):
        hum += GPIO.input(hum_pin)
        time.sleep(0.1)
    hum = hum / 10.0
    return hum

# Leer la humedad del suelo
try:
    while True:
        hum = read_humidity()
        print("Humedad del suelo:", hum)
        time.sleep(3)
except KeyboardInterrupt:
    pass
