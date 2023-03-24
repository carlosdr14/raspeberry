import RPi.GPIO as GPIO
import time
from lista import LISTA
from jsonHandler import JSONHandler
from mongoConexion import CheckInternet
import pymongo

class Led (LISTA,JSONHandler):
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)

    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)
        print("LED encendido")
        return True

    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)
        print("LED apagado")
        return False

    def parpadear(self, tiempo_encendido, tiempo_apagado, repeticiones):
        try:
            for i in range(repeticiones):
                GPIO.output(self.pin, GPIO.HIGH)
                time.sleep(tiempo_encendido)
                GPIO.output(self.pin, GPIO.LOW)
                time.sleep(tiempo_apagado)
        except KeyboardInterrupt:
            print("Se ha detenido el parpadeo")
            
    def limpiar(self):
        GPIO.cleanup()
    def check_internet(self, estado):
        check_internet = CheckInternet()
        status, message = check_internet.is_connected()
        json_handler = JSONHandler("localLed.json")
        d = {"Estado": estado, "Fecha": time.strftime("%d/%m/%y"), "Hora": time.strftime("%H:%M:%S")}
        if status:
            client = pymongo.MongoClient("mongodb+srv://admin:1234admin@cluster0.qf2sgqk.mongodb.net/test")
            db = client["Raspberry"]
            collection = db['Led']
            print("Connected to MongoDB")
            self.agregar(d)
            self.save(d)
            collection.insert_one(d)
        else:
            print(message)
            try:
                existing_data = json_handler.open()
                existing_data.append(d)
                json_handler.save(existing_data)
            except:
                json_handler.save([d])

    def menu (self):
        print("1. Encender")
        print("2. Apagar")
        print("3. Parpadear")
        print("4. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    
    def run(self):

        while True:
            opcion = self.menu()
            if opcion == 1:
                estado=self.encender()
                self.check_internet(estado)
            elif opcion == 2:
                estado=self.apagar()
                self.check_internet(estado)
            elif opcion == 3:
                self.parpadear(0.5, 0.5, 5)
            elif opcion == 4:

                break
            else:
                print("Opcion no valida")
       



