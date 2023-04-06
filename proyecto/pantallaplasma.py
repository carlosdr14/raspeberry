import serial
from time import sleep
from Adafruit_Python_CharLCD import Adafruit_CharLCD

# Configuración del puerto serie para el Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)

# Configuración de la pantalla de plasma
lcd_rs        = 26  
lcd_en        = 19
lcd_d4        = 13
lcd_d5        = 6
lcd_d6        = 5
lcd_d7        = 11
lcd_columns   = 16
lcd_rows      = 2
lcd           = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

# Bucle principal
while True:
    # Lee los datos del Arduino
    distance = arduino.readline().strip()
    # Muestra los datos en la pantalla de plasma
    lcd.clear()
    lcd.message('Distancia:\n{} cm'.format(distance))
    # Espera un segundo antes de actualizar los datos
    sleep(1)
