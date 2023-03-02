import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)
        print("LED encendido")

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)
        print("LED apagado")

    def parpadear(self, duracion_encendido, duracion_apagado, repeticiones):
        for i in range(repeticiones):
            self.encender()
            time.sleep(duracion_encendido)
            self.apagar()
            time.sleep(duracion_apagado)

    def limpiar(self):
        GPIO.cleanup()

# Ejemplo de uso
led = Led(18)
led.encender()
time.sleep(5)
led.apagar()
led.parpadear(0.5, 0.5, 5)
led.limpiar()
