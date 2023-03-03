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
try:
    while True:
        # Preguntar al usuario si desea prender o apagar el LED
        action = input("Ingrese 'on' para prender el LED, 'off' para apagarlo, o 'exit' para salir: ")
        
        # Ejecutar la acción correspondiente
        if action == "on":
            led.on()
            led.encender()
        elif action == "off":
            led.off()
            led.apagar()
        elif action == "exit":
            break
        else:
            print("Acción no válida.")
    
except KeyboardInterrupt:
    pass

# Limpiar el pin del LED antes de salir
led.cleanup()
