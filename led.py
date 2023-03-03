import RPi.GPIO as GPIO
import time

class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
    
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
    
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
    
    def cleanup(self):
        GPIO.cleanup(self.pin)

# Crea un objeto LED para el pin 11
led = LED(18)

try:
    while True:
        # Preguntar al usuario si desea prender o apagar el LED
        action = input("Ingrese 'on' para prender el LED, 'off' para apagarlo, o 'exit' para salir: ")
        
        # Ejecutar la acción correspondiente
        if action == "on":
            led.on()
        elif action == "off":
            led.off()
        elif action == "exit":
            break
        else:
            print("Acción no válida.")
    
except KeyboardInterrupt:
    pass

# Limpiar el pin del LED antes de salir
led.cleanup()


