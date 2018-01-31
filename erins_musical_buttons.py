#Erin J Sinclair
#011618
#Musical Buttons
#Press a button to hear music!


# import needed libraries
import RPi.GPIO as GPIO
import time
import random
import os
def get_MP3_sounds(sounds_path):
    sound_files=os.listdir(sounds_path)
    sound_files= [sound_file for sound_file in sound_files if sound_file.endswith('.mp3')]
    return sound_files

def play_random_sound (sound_path, sound_files):
    sound_file=random.choice(sound_files)
    command = "omxplayer -o local '" + sound_path + "/" + sound_file + "' &"
    print(command)
    os.system(command)

path_music = "/usr/share/scratch/Media/Sounds/Music Loops"
path_vocals = "/usr/share/scratch/Media/Sounds/Vocals"
path_effects = "/usr/share/scratch/Media/Sounds/Effects"

sounds_music = get_MP3_sounds(path_music)
sounds_vocals = get_MP3_sounds(path_vocals)
sounds_effects =get_MP3_sounds(path_effects)

print (sounds_music)
print (sounds_vocals)
#Variables for button pins
button_pin1 = 6
button_pin2 =19

#Set pin numbering
GPIO.setmode (GPIO.BCM)

#Setup GPIO for input
GPIO.setup (button_pin1, GPIO.IN)
GPIO.setup (button_pin2, GPIO.IN)


os.system("clear")

print ("""Welcome to Musical Buttons! Press button 1 to play music,
       and press button 2 for vocals! Press Ctrl + C to exit.""")
while True:
    if GPIO.input(button_pin1):
        print ("You pressed button 1")
        play_random_sound(path_music, sounds_music)
        time.sleep(0.1)
    if GPIO.input(button_pin2):
        print ("You pressed button 2")
        play_random_sound(path_vocals, sounds_vocals)
        time.sleep(0.1)
        time.sleep(0.1)
    if GPIO.input(button_pin2) and GPIO.input(button_pin1):
        print ("You pressed buttons 1 and 2! Easter Egg!")
        play_random_sound(path_effects, sounds_effects)
        time.sleep(0.1)
    time.sleep(0.1)
