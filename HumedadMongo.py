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

    def insertar_en_mongo(self, datos_sensor):
        # Conectar con una instancia de MongoDB
        client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")

        # Seleccionar una base de datos y una colección
        db = client["sensores"]
        coleccion = db["datos_sensores"]

        # Insertar los datos en la colección
        coleccion.insert_one(datos_sensor)
        
    def guardar_en_json(self, datos_sensor):
        with open('datos_sensor.json', 'a') as file:
            json.dump(datos_sensor, file)
            file.write('\n')
        
    def temHum(self):
        print("Temperatura y humedad")
        temperatura = Temperatura()
        datos = temperatura.get_temperatura_humedad()
        print("Temperatura: ", datos["temperatura"], "C")
        print("Humedad: ", datos["humedad"], "%")
        
        # Insertar los datos en MongoDB
        temperatura.insertar_en_mongo(datos)
        
        # Guardar los datos en un archivo JSON
        temperatura.guardar_en_json(datos)

if __name__ == "__main__":
    temperatura = Temperatura()
    temperatura.temHum()
