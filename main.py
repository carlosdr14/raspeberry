from led import Led
from distancia import UltrasonicSensor
from mongoConexion import CheckInternet
from jsonHandler import JSONHandler
import pymongo
import RPi.GPIO as GPIO
class Main:
    def __init__(self):
        
        
        self.led = Led(19)
        self.ultrasonic_sensor = UltrasonicSensor(18, 24, "DistanciaLocal.json")
       

    def menu(self):
        print("1. Led")
        print("2. Distancia")
        print("3. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    
    def check_internet(self):
        sensorUltrasonico= JSONHandler("locallLed.json")
        Led= JSONHandler("localLed.json")
        check_internet = CheckInternet()
        if check_internet.is_connected():
            print("Hay internet")
            client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
            db = client["Raspberry"]
            collection=db['Ultrasonico']
            collection2=db['Led']
            print("Connected to MongoDB")
            try:
               ultra=sensorUltrasonico.open()
              #
               for i in ultra:
                 collection.insert_one(i)
               sensorUltrasonico.save([])

               for i in Led:
                 collection2.insert_one(i)
            
               Led.save([])

            except:
                pass
  
        else:
            print("No hay internet")
          



    def run(self):
        while True:
            self.check_internet()

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
        self.ultrasonic_sensor.limpiar()


main = Main()
main.run()

