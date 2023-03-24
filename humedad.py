import time
import board
import adafruit_dht
import pymongo
from mongoConexion import CheckInternet
from jsonHandler import JSONHandler
from lista import Lista


class DHTSensor(Lista, JSONHandler):
    def __init__(self, pin, file_name):
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.file_name = file_name

    def get_temperatures(self):
        try:
            temperature_c = self.dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.dhtDevice.humidity
            return temperature_f, temperature_c, humidity
        except RuntimeError as error:
            print(error.args[0])
            return None

    def check_internet(self, temperature_c, temperature_f, humidity):
        check_internet = CheckInternet()
        status, message = check_internet.is_connected()
        d = {
            "Temperatura": temperature_c,
            "Fahrenheit": temperature_f,
            "Humedad": humidity,
            "Fecha": time.strftime("%d/%m/%y"),
            "Hora": time.strftime("%H:%M:%S")
        }

        if status:
            client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
            db = client["Raspberry"]
            collection = db['Temperatura']
            print("Connected to MongoDB")
          
            collection.insert_one(d)
        else:
            print(message)
            try:
                products = self.open(self.file_name)
                products.append(d)
                self.save(products, self.file_name)
            except:
                self.save([d], self.file_name)

    def run(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                temperatures = self.get_temperatures()
                if temperatures is not None:
                    self.check_internet(*temperatures)
                    print("Temperatura F: {:.1f}, Temperatura C: {:.1f}, Humedad: {}%".format(*temperatures))
            elif opcion == 2:
                break
            else:
                print("Opcion no valida")

    def menu(self):
        print("1. Temperatura y humedad")
        print("2. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
