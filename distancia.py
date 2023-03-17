import RPi.GPIO as GPIO
import time

from mongoConexion import CheckInternet
import pymongo
from jsonHandler import JSONHandler
from lista import Lista

import RPi.GPIO as GPIO

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin, filename):
        super().__init__()

        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.filename = filename

        # Set up GPIO mode
        GPIO.setmode(GPIO.BCM)  # or GPIO.setmode(GPIO.BOARD)

        # Set up trigger and echo pins as output and input, respectively
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)



    def measure_distance(self):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2

        return distance
    
    def menu (self):
        
        print("1. Medir distancia")
        print("2. Medir distancia continuamente")
        print("3. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    
    #funcion que cheque si hay internet guardando en la base de datos y si no hay internet guarda en un archivo
    def check_internet(self, distance):
        d=distance
        
        json_handler = JSONHandler("DistanciaLocal.json")
        check_internet = CheckInternet()
        if check_internet.is_connected():
            print("Hay internet")
            client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
            db = client["Raspberry"]
            collection=db['UltasonicSensor']
            print("Connected to MongoDB")
            self.agregar(d)
            self.save(d)  # pass the distance argument
            collection.insert_one(d)
            try:
                products = json_handler.open()
                for p in products:
                    collection.insert_one(p)
                # Clear the JSON file after submitting the products
                json_handler.save([])
            except:
                pass
        else:
            print("No hay internet")
            try:
             products = json_handler.open()
             products.append(d)
             json_handler.save(products)
            except:
                json_handler.save([d])



    def run(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                dist = self.measure_distance()
                print("Measured Distance = %.1f cm" % dist)
                dis= {"Distancia": dist, "cm": "cm", "Fecha": time.strftime("%d/%m/%y"), "Hora": time.strftime("%H:%M:%S")}
                self.check_internet(dis)
            elif opcion == 2:
                self.run_continuous()
            elif opcion == 3:
                break
            else:
                print("Opcion no valida")
        self.__del__()

        

    def run_continuous(self):
        try:
            while True:
                dist = self.measure_distance()
                print("Measured Distance = %.1f cm" % dist)
                time.sleep(3)
        except KeyboardInterrupt:
            print("Measurement stopped by User")
            self.__del__()

    def __del__(self):
        GPIO.cleanup()

    


