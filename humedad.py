import time
import board
import adafruit_dht

class DHTSensor:
    def __init__(self, pin):
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.running = False

    def getTempeture(self):
        self.running = True

        while self.running:
            try:
                temperature_c = self.dhtDevice.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = self.dhtDevice.humidity
                return("Temp: {:.1f} F / {:.1f} C    Humidity: {}% "
                      .format(temperature_f, temperature_c, humidity))
            except RuntimeError as error:
                print(error.args[0])
            time.sleep(2.0)



    def run(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                self.getTempeture()
                print (self.getTempeture())

            elif opcion == 2:
                break
            else:
                print("Opcion no valida")
        


    def menu(self):
        print("1. Temperatura y humedad")
        print("2. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
   

  