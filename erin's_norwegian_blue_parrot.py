# Erin Sinclair
# 101817
# Norwegian Blue Parrot
# A guessing game

import random


print ("Welcome to the Norwegian Blue Parrot!")

instructions=""" As you are shopping in London, you walk into an old, smelly
       pet shop. As the door closes behind you,
       you see a beautiful blue parrot sitting very still in a cage. The pet 
       shop owner greets you and says: 'Today is your lucky day! If you can
       guess the age of this Norwegian Blue Parrot, you get to take it for
       free! Would you like to try? You only get 5 guesses?' You nod. 'Great!
       You can start right... NOW!'""" 

print (instructions)
# Make up parrot's age
parrot_age = random.randint (1, 50)

#Set guesses to 0
number_of_guesses = 0

while number_of_guesses < 5:
    # Get a guess from the user
    guess = input ("Guess the age of the parrot [1 to 50]:")
    guess = int(guess)# Converts a string into an integer
    number_of_guesses = number_of_guesses + 1
    print(number_of_guesses)
    if guess == parrot_age:
        print("'Great job! You may take your Norweigen Blue Parrot!'")
        break
    else:
        if guess < parrot_age:
            print ("'What! You think my parrot is that young? I is most certainly not!'")
        else:
            print ("'I could not keep a bird alive that long!'")
        print("'That was a horrible guess, you silly person!'")
      
print ("Thank you for playing! The parrot was " , parrot_age , " years old")

