import time
import board
import adafruit_dht
import pymongo
import json
from mongoConexion import CheckInternet
from jsonHandler import JSONHandler
from lista import LISTA
import os.path

class DHTSensor(LISTA, JSONHandler):
    def __init__(self, pin, file_name,Pin):
        super().__init__()
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.file_name = file_name
        self.pin = Pin

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
 
        # Check if the file exists
        if not os.path.isfile('localTemperatura.json'):
            # If the file doesn't exist, create an empty list
            data = []
        else:
            # If the file exists, read the existing data from the file
            with open('localTemperatura.json', 'r') as f:
                data = json.load(f)

        # Append the new data to the existing data
        d = {
            "Nombre": "DHT11",
            "Temperatura": temperature_c,
            "Fahrenheit": temperature_f,
            "Humedad": humidity,
            "Fecha": time.strftime("%d/%m/%y"),
            "Hora": time.strftime("%H:%M:%S"),
            "Pin": self.pin,
            "Ubicacion": "Dentro del Carrito"
        }
        data.append(d)

        # Write the updated data back to the file
        with open('localTemperatura.json', 'w') as f:
            json.dump(data, f)


    def limpiar(self):
        self.dhtDevice.exit()

    def run(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                temperatures = self.get_temperatures()
                if temperatures is not None:
                    self.check_internet(*temperatures)
                    print("Temperatura F: {:.1f}, Temperatura C: {:.1f}, Humedad: {}%".format(*temperatures))
                    self.check_internet(*temperatures)

                    
            elif opcion == 2:
                break
            else:
                print("Opcion no valida")

    def menu(self):
        print("1. Temperatura y humedad")
        print("2. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
