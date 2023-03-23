import pymongo
from datetime import datetime
import Adafruit_DHT
import RPi.GPIO as GPIO
import json

class Temperatura:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = 5
        GPIO.setmode(GPIO.BCM)

    def get_temperatura_humedad(self):
        temperatura, humedad = Adafruit_DHT.read(self.sensor, self.pin)
        if temperatura is not None and humedad is not None:
            datos = {"temperatura": temperatura, "humedad": humedad, "fecha": datetime.now()}
            return datos
        else:
            return {"temperatura": 0, "humedad": 0, "fecha": datetime.now()}
        
    def temHum(self):
        print("Temperatura y humedad")
        temperatura = Temperatura()
        datos = temperatura.get_temperatura_humedad()
        print("Temperatura: ", datos["temperatura"], "C")
        print("Humedad: ", datos["humedad"], "%")
        
    def menu (self):
        print("1. Temperatura y humedad")
        print("2. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    
    def run(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                self.temHum()
            elif opcion == 2:
                break
            else:
                print("Opcion no valida")
    


