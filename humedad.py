import time
import board
import adafruit_dht

class DHTSensor:
    def __init__(self, pin):
        self.dhtDevice = adafruit_dht.DHT11(pin)
        self.running = False

    def run(self):
        try:
            temperature_c = self.dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = self.dhtDevice.humidity
            print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% "
                .format(temperature_f, temperature_c, humidity))
        except RuntimeError as error:
            print(error.args[0])

        while True:
            try:
                time.sleep(2.0)
            except KeyboardInterrupt:
                print("Programa interrumpido por el usuario.")
                break


    def menu(self):
        print("1. Temperatura y humedad")
        print("2. Salir")
        opcion = int(input("Ingrese una opcion: "))
        return opcion
    def runn(self):
        while True:
            opcion = self.menu()
            if opcion == 1:
                self.run()
            elif opcion == 2:
                break

    def stop(self):
        self.running = False

