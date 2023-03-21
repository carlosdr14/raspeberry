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
        self.check_internet = CheckInternet()

    def menu(self):
        print("1. Led")
        print("2. Distancia")
        print("3. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    
    def check_internet(self, file_name, file_name2):
        ultar= JSONHandler("DistanciaLocal.json")
        Led= JSONHandler("LedLocal.json")
        check_internet = CheckInternet()
        if check_internet.is_connected():
            print("Hay internet")
            client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
            db = client["Raspberry"]
            collection=db['UltasonicSensor']
            collection2=db['Led']
            print("Connected to MongoDB")
            # pass the distance argument
            try:
               ultra =  ultar.open()
               led = Led.open()
               for i in ultra:
                   collection.insert_one({"Distancia": i})
               ultra.save([])
               for i in led:
                     collection2.insert_one({"Led": i})
               led.save([])

            except:
                print("No hay datos en el archivo")
  
        else:
            print("No hay internet")
          



    def run(self):
        while True:
            self.check_internet("DistanciaLocal.json", "LedLocal.json")

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

