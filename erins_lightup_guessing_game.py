
#Light-up Guessing Game
#Erin J. Sinclair
#010318
#Guess the number (1-20) in 5 tries! 

import time
import random
import RPi.GPIO as GPIO

def game_over():
    '''my game over function'''
    print ("You ran out of guesses.")
    blink_led(LED_pin_red)
def blink_led(pin):
    for i in range(5):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.2)
def blink_Yellow():
    pwm_red=GPIO.PWM(LED_pin_red, 100)
    pwm_green=GPIO.PWM(LED_pin_green, 100)
    pwm_blue=GPIO.PWM(LED_pin_blue, 100)
    pwm_red.start(50)
    pwm_green.start(100)
    pwm_blue.start(0)
    time.sleep(5)
    pwm_red.stop()
    pwm_blue.stop()
    pwm_green.stop()
def easter_egg(LED_pin_green, LED_pin_blue, LED_pin_red):
    for i in range(20):
        GPIO.output(LED_pin_green,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED_pin_blue,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED_pin_red,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(LED_pin_green,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(LED_pin_blue,GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(LED_pin_red,GPIO.LOW)
        time.sleep(0.2)
    GPIO.output(LED_pin_red,GPIO.LOW)
    GPIO.output(LED_pin_green,GPIO.LOW)
    GPIO.output(LED_pin_blue,GPIO.LOW)

    
#LED setup

GPIO.setmode (GPIO.BCM)
LED_pin_red=21
LED_pin_green=22
LED_pin_blue=23

GPIO.setup (LED_pin_red, GPIO.OUT)
GPIO.setup (LED_pin_green, GPIO.OUT)
GPIO.setup (LED_pin_blue, GPIO.OUT)
#Title screen and instructions
play_again="YES"

print ("""Welcome to the Light-Up Guessing Game! You have 5
guesses to guess a number from 1 to 20. If you guess to high,
the light will flash red. If you guess to low, the light will
turn blue. If you guess correctly, the light will blink green.
Good luck!""")

while play_again=="YES" or play_again==" YES":
    #Get random number (1-20)

    num = random.randint(1,20)

    #Start loop (5 tries)
    guesses = 0
    while guesses < 6:
        
        #Get a guess from the user
        guess=input("Guess a number from 1 to 20:")
        if guess == "goat":
            easter_egg(LED_pin_green, LED_pin_blue,LED_pin_red)
            break
        if guess.isdigit():
            guess = int (guess)
        guesses += 1
        #Check if correct, too low, or too high
        if guess == num:
            print("You are correct!")
            #TODO: blink green
            blink_led(LED_pin_green)
            break
        elif guess < num:
            print ("Too low.")
            #TODO: blink blue
            blink_led(LED_pin_blue)
        elif guess > num:
            print ("Too high.")
            #TODO: blink red
            blink_led(LED_pin_red)
        else:
            blink_Yellow
            print("Please type a number from 1-20")
    else:
        game_over()
    play_again=input("Would you like to play again?").upper()
print("Thanks for playing the Light-Up Guessing Game! Good bye for now!")
#Flash the appropriate color for 3 seconds
