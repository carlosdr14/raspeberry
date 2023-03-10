import Adafruit_DHT
import RPi.GPIO as GPIO

class Temperatura:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = 17
        GPIO.setmode(GPIO.BCM)

    def get_temperatura_humedad(self):
        temperatura, humedad = Adafruit_DHT.read(self.sensor, self.pin)
        if temperatura is not None and humedad is not None:
            datos = [temperatura, humedad]
            return datos
        else:
          return[0,0]
        
    def temHum(self):
        print("Temperatura y humedad")
        temperatura = Temperatura()
        datos = temperatura.get_temperatura_humedad()
        print("Temperatura: ", datos[0], "C")
        print("Humedad: ", datos[1] , "%")
    
if __name__ == "__main__":
    temperatura = Temperatura()
    temperatura.temHum()
