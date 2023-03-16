import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        GPIO.setmode(GPIO.BCM)
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)

    def measure_distance(self):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop_time = time.time()

        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2

        return distance

    def run_continuous(self):
        try:
            while True:
                dist = self.measure_distance()
                print("Measured Distance = %.1f cm" % dist)
                time.sleep(2)
                print("To stop the measurement press CTRL+C")
        except KeyboardInterrupt:
            print("Measurement stopped by User")
            self.__del__()

    def __del__(self):
        GPIO.cleanup()

    



sensor = UltrasonicSensor(18, 24)
sensor.run_continuous()
