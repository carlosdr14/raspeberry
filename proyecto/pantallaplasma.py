from time import sleep
from Adafruit_Python_CharLCD import Adafruit_CharLCD
from gpiozero import DistanceSensor

# Configuración de la pantalla de plasma
lcd_rs        = 26  
lcd_e        = 19
lcd_d4        = 13
lcd_d5        = 6
lcd_d6        = 5
lcd_d7        = 11
lcd_columns   = 16
lcd_rows      = 2
lcd           = Adafruit_CharLCD(lcd_rs, lcd_e, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Configuración del sensor de ultrasonido
sensor = DistanceSensor(echo=17, trigger=4)

# Bucle principal
while True:
    # Lee la distancia medida por el sensor en metros
    distance = sensor.distance
    # Convierte la distancia a centímetros
    distance_cm = round(distance * 100, 1)
    # Muestra los datos en la pantalla de plasma
    lcd.clear()
    lcd.message('Distancia:\n{} cm'.format(distance_cm))
    # Espera un segundo antes de actualizar los datos
    sleep(1)
