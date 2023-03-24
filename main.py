from led import Led
from distancia import UltrasonicSensor
from humedad import DHTSensor
from mongoConexion import CheckInternet
from jsonHandler import JSONHandler
import pymongo
import RPi.GPIO as GPIO
import board
from jsonHandler import JSONHandler
class Main:
    def __init__(self,JsonHandler):
        
        
        self.led = Led(19, "localLedd.json")
        self.ultrasonic_sensor = UltrasonicSensor(18, 24, "localDistance.json")
        self.temperatura = DHTSensor(board.D16,"localTemperatura.json",16)
       

    def menu(self):
        print("1. Led")
        print("2. Distancia")
        print("3. Temperatura y humedad")
        print("4. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    
    def check_internet(self):
        sensorUltrasonico = JSONHandler("localDistance.json")
        check_internet = CheckInternet()
        if check_internet.is_connected():
            print("Hay internet")
            with pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test") as client:
                db = client["Raspberry"]
                collection = db['SensorsData']
                try:
                    ultra = sensorUltrasonico.open()
                    for i in ultra:
                        data = {"sensor": "ultrasonico", "data": i}
                        collection.insert_one(data)
                    sensorUltrasonico.save([])

                except:
                    pass

        else:
            print("No hay internet")


    def check_internet2(self):
        
        Led = JSONHandler("localLedd.json")
       
        check_internet = CheckInternet()
        if check_internet.is_connected():
            print("Hay internet")
            with pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test") as client:
                db = client["Raspberry"]
                collection = db['SensorsData']
                try:
                    led= Led.open()
                    for i in led:
                     collection.insert_one(i)
                    Led.save([])

              

                except:
                    pass

        else:
            print("No hay internet")
    def check_internet3(self):
        
        Temperatura = JSONHandler("localTemperatura.json")
        check_internet = CheckInternet()
        if check_internet.is_connected():
            print("Hay internet")
            with pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test") as client:
                db = client["Raspberry"]
                collection = db['SensorsData']
                try:
                    tem= Temperatura.open()
                    for i in tem:
                        collection.insert_one(i)
                   
                    
                    Temperatura.save([])

              

                except:
                    pass

        else:
            print("No hay internet")



    def run(self):
        while True:
            self.check_internet()
            self.check_internet2()
            self.check_internet3()
            opcion = self.menu()
            if opcion == 1:
               self.led.run()
            elif opcion == 2:
                self.ultrasonic_sensor.run()
            elif opcion == 3:
                self.temperatura.run()
            elif opcion == 4:



                break
            else:
                print("Opcion no valida")
        self.led.limpiar()
        self.ultrasonic_sensor.limpiar()
        self.temperatura.limpiar()


main = Main()
main.run()

