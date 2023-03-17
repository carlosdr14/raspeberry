import RPi.GPIO as GPIO
import time

from mongoConexion import CheckInternet
import pymongo
from jsonHandler import JSONHandler
from lista import Lista


class UltrasonicSensor(Lista,JSONHandler):
    def __init__(self, trigger_pin, echo_pin, file_name):
        super().__init__()
        GPIO.setmode(GPIO.BCM)
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)
        self.file_name = file_name

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
    def check_internet(self):
     json_handler = JSONHandler("DistanciaLocal.json")
     check_internet = CheckInternet()
     if check_internet.is_connected():
        print("Hay internet")
        
        client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
        db = client["Raspberry"]
        collection = db['UltasonicSensor']
        print("Connected to MongoDB")
        distance = {"Distancia": self.measure_distance(), "Unidad": "cm", "Fecha": time.strftime("%d/%m/%y"), "Hora": time.strftime("%H:%M:%S")}
        self.agregar(distance)
        self.save(distance)
        collection.insert_one(distance)

        try:
            products = json_handler.open()
            for p in products:
                collection.insert_one(p)
            # Clear the JSON file after submitting the products
            json_handler.save([])
        except:
            pass

        self.save()
     else:
        print("No hay internet")
        distance = ["Distancia", self.measure_distance(), "cm", "Fecha", time.strftime("%d/%m/%y"), "Hora", time.strftime("%H:%M:%S")]
        self.agregar(distance)
        self.save(distance)
        self.save()



    def run(self):


        while True:
            opcion = self.menu()
            if opcion == 1:
                dist = self.measure_distance()
                print("Measured Distance = %.1f cm" % dist)
                self.check_internet()

                
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

    


