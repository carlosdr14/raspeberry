import Adafruit_DHT

# Configuración del sensor
sensor = Adafruit_DHT.DHT22
pin = 4

# Lectura de los valores de humedad y temperatura
humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

# Mostrar los valores de humedad y temperatura
if humedad is not None and temperatura is not None:
    print('Temperatura={0:0.1f}°C Humedad={1:0.1f}%'.format(temperatura, humedad))
else:
    print('Error al leer los valores. Intenta de nuevo!')


#Libraries
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
DHT_PIN = 17
 
def read_sensor():
    # read sensor data
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
 
    return temperature, humidity
 
try:
     while True:
      temperature, humidity = read_sensor()
      print("Temperature = {:.1f}°C, Humidity = {:.1f}%".format(temperature, humidity))
      time.sleep(2)
 
# Reset by pressing CTRL + C
except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
