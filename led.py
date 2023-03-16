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

    def parpadear(self, tiempo_encendido, tiempo_apagado, repeticiones):
        for i in range(repeticiones):
            self.encender()
            time.sleep(tiempo_encendido)
            self.apagar()
            time.sleep(tiempo_apagado)



    def limpiar(self):
        GPIO.cleanup()

        
    def menu (self):
        print("1. Encender")
        print("2. Apagar")
        print("3. Parpadear")
        print("4. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    
    def run(self):

        while True:
            opcion = self.menu()
            if opcion == 1:
                self.encender()
            elif opcion == 2:
                self.apagar()
            elif opcion == 3:
                self.parpadear(0.5, 0.5, 5)
            elif opcion == 4:
                break
            else:
                print("Opcion no valida")
        self.limpiar()



led = Led(19)
led.run()
