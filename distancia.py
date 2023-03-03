import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BOARD)
GPIO_TRIGGER = 11
GPIO_ECHO = 13
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distancia():
    # Poner el trigger en bajo
    GPIO.output(GPIO_TRIGGER, False)

    # Esperar un momento para permitir que el sensor se estabilice
    time.sleep(0.5)

    # Enviar un pulso al sensor
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    # Esperar a que el sensor envíe una señal de retorno
    start_time = time.time()
    end_time = 0
    while GPIO.input(GPIO_ECHO) == 0:
        if time.time() - start_time > 1:
            break

    while GPIO.input(GPIO_ECHO) == 1:
        end_time = time.time()

    # Calcular la duración del pulso
    pulse_duration = end_time - start_time

    # Calcular la distancia en base a la duración del pulso
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

# Ejemplo de uso de la función distancia
try:
    while True:
        print("Distancia:", distancia(), "cm")
        time.sleep(3)

except KeyboardInterrupt:
    pass

# Limpieza de los pines GPIO
GPIO.cleanup()
