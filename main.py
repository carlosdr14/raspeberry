from distancia import UltrasonicSensor
from led import Led
import humedad


class Menu():
    def __init__(self):
        pass
 

    def menu(self):
        print("1. Humedad")
        print("2. Distancia")
        print("3. Led")
        print("4. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            self.humedad()
        elif opcion == 2:
            UltrasonicSensor.menu()
        elif opcion == 3:
            Led.menu()
        elif opcion == 4:
            exit()
        else:
            print("Opcion invalida")
            self.menu()

menu = Menu()
menu.menu()