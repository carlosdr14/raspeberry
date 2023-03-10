import Adafruit_DHT  
import time  
 
while True:
  sensor = Adafruit_DHT.DHT11 
  pin = 17 
  humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
 
  print ('Humedad: ' , humedad)
  print ('Temperatura: ' , temperatura)
  
  time.sleep(1) 
  humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin, platform=Adafruit_DHT.DHT22.AM2302)
