#Erin Sinclair
#10 / 11/ 2017
#Silly Sentence Generator 3000
#Makes silly sentences like a madlib

print ("*" * 48)
print ("* Welcome to the Silly Sentence Generator 3000! *")
print ("*" * 48)

# getting the player's name
player_name=input("please enter your name:")

# + can add or join strings together.
message = "Hello," + player_name + "! Let's make a Silly Sentence !"
print(message)

# gather input from user
famous_person = input("Enter the name of a famous person:")
adjective1 = input("Enter an adjective:")
adjective2 = input("Enter another adjective:")
verb= input("Enter a verb inding in -ING:")

silly_sentence = ("The " + adjective1 + " " + "blue " + player_name +
                  + " is " + verb + " the " + adjective2 + " " + famous_person)

print(silly_sentence)

