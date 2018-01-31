import RPi.GPIO as GPIO
import time

LED_pin_red = 21
LED_pin_green = 22
LED_pin_blue = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_pin_red,GPIO.OUT)
GPIO.setup(LED_pin_green,GPIO.OUT)
GPIO.setup(LED_pin_blue,GPIO.OUT)

while True:
    GPIO.output(LED_pin_red, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_pin_green, GPIO.HIGH)
    time.sleep (1)
    GPIO.output(LED_pin_blue, GPIO.HIGH)
    time.sleep(1)
    print ("On")
    time.sleep(1)
    GPIO.output(LED_pin_red, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED_pin_green, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED_pin_blue, GPIO.LOW)
    time.sleep(1)
    print ("Off")
    time.sleep(1)

