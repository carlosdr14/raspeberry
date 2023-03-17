from led import Led
from distancia import UltrasonicSensor
from mongoConexion import CheckInternet
import RPi.GPIO as GPIO
class Main:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.led = Led(19)
        self.ultrasonic_sensor = UltrasonicSensor(18, 24, "DistanciaLocal.json")
        self.check_internet = CheckInternet()

    def menu(self):
        print("1. Led")
        print("2. Distancia")
        print("3. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion

    def run(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                self.led.run()
            elif opcion == 2:
                self.ultrasonic_sensor.run()
            elif opcion == 3:
                break
            else:
                print("Opcion no valida")
        self.led.limpiar()
        self.ultrasonic_sensor.__del__()


main = Main()
main.run()

