import RPi.GPIO as GPIO

led = 26
photoresistor = 6
state = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(photoresistor, GPIO.IN)

while True:
    GPIO.output(led, not(GPIO.input(photoresistor)))