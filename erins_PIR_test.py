#PIR Test
#Erin J Sinclair
#012418

import RPi.GPIO as GPIO
import time

detect_mode=False

PIR_pin=12
LED_pin = 21
button_pin = 6

GPIO.setmode (GPIO.BCM)
GPIO.setup (PIR_pin, GPIO.IN)
GPIO.setup (LED_pin, GPIO.OUT)
GPIO.setup (button_pin, GPIO.IN)


while True:
    if detect_mode==True:
        print ("detecting")
        if  GPIO.output(LED_pin, GPIO.HIGH):
                time.sleep (0.5)
        else:
                GPIO.output(LED_pin, GPIO.LOW)
                time.sleep(0.5)
    if GPIO.input (button_pin):
        if detect_mode == True:
            detect_mode = False
        else:
            detect_mode = True 
    time.sleep(0.5)
           

#GPIO.input (PIR_pin):print ("Motion detected")
