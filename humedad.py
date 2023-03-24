import time
import board
import adafruit_dht
from mongoConexion import CheckInternet
from jsonHandler import JSONHandler
import pymongo
from lista  import Lista

class DHTSensor(JSONHandler, Lista):
    def __init__(self, pin,file_name):
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.running = False
        self.file_name = file_name

    def getTempeture(self):
        self.running = True

        while self.running:
            try:
                temperature_c = self.dhtDevice.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = self.dhtDevice.humidity
                return(temperature_f, temperature_c, humidity)
            except RuntimeError as error:
                print(error.args[0])
            time.sleep(2.0)


    def check_internet(self, temperature_c, temperature_f, humidity):
        check_internet = CheckInternet()
        status, message = check_internet.is_connected()
        json_handler = JSONHandler("localDistance.json")
        d= {"Temperatura": temperature_c, "Fahrenheit": temperature_f, "Humedad": humidity, "Fecha": time.strftime("%d/%m/%y"), "Hora": time.strftime("%H:%M:%S")}
       
        if status:
            client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
            db = client["Raspberry"]
            collection=db['Temperatura']
            print("Connected to MongoDB")
            self.agregar(d)
            self.save(d)
            collection.insert_one(d)
           



    def run(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                temperaturas=self.getTempeture()
                self.check_internet(temperaturas[0], temperaturas[1], temperaturas[2])
                print ("Temperatura: {:.1f} F / {:.1f} C   Humidity: {}% ".format(temperaturas[0], temperaturas[1], temperaturas[2]))

            elif opcion == 2:
                break
            else:
                print("Opcion no valida")
        


    def menu(self):
        print("1. Temperatura y humedad")
        print("2. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
   

  