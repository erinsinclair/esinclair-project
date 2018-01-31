# Erin J. Sinclair
#110117
# Combonation Lock
# A  Guessing Game: you must crack the code on the lock!

import random

print ("Welcome to Combonation Lock!")
print ("""You are detective, trying to uncover secrets in a
    rickety old mansion. You enter the basement, where you see a
    painting contrasting odly with the color of the wall. It is
    tilting to one side as if someone placed it there in a hurry.
    curiously, you lift it off the wall. And then you see a safe.
    You test it for fingerprints, and immidiately find it is covered
    with those of the criminal. You try to open it, but it's locked.
    The lock is a combination lock. It has four didgets. You know the
    criminal will return to his house at any moment, and he'll find
    you right away. But you really need to know what is in the safe.
    Can you solve it in time?""")
guesses1=0
guesses2=0
guesses3=0
guesses4=0
didget_1= random.randint (0, 9)
didget_2= random.randint (0, 9)
didget_3= random.randint (0, 9)
didget_4= random.randint (0, 9)


#TODO: add breaks and edit messages.

while guesses1 < 5:
    # Get a guess from the user
    guess = input ("You have one minute. Guess a number[0-9]:")
    guess = int(guess)# Converts a string into an integer
    guesses1 = guesses1 + 1
    print(guesses1)
    if guess == didget_1:
        print("Correct! Now try didget 2!")
    else:
          if guess > diget_1:
            print ("Try a smaller number.")
        else:
            print ("Try a larger number.")
    
 while guesses2 < 5:
    # Get a guess from the user
    guess = input ("You have one minute. Guess a number[0-9]:")
    guess = int(guess)# Converts a string into an integer
    guesses2 = guesses2 + 1
    print(guesses2)
     if guess == didget_2:
        print("Correct! Now crack the third didget!")
        break
     else:
        if guess > diget_2:
            print ("Try a smaller number.")
         else:
            print ("Try a larger number.")

while guesses3 < 5:
    # Get a guess from the user
    guess = int(guess)# Converts a string into an integer
    guesses3 = guesses3 + 1
    print(guesses3)
     if guess == didget_3:
        print("Correct! Now solve the last didget!")
    else:
          if guess > diget_3:
            print ("Try a smaller number.")
          else:
            print ("Try a larger number.")
while guesses4 < 5:
    # Get a guess from the user
    guess = input ("You have one minute. Guess a number[0-9]:")
    guess = int(guess)# Converts a string into an integer
    guesses3 = guesses4 + 1
    print(guesses4)
    if guess == didget_4:
        print("Correct! Now try the next one!")
     else:
         if guess > diget_4:
            print ("Try a smaller number.")
        else:
            print ("Try a larger number.")
print ("Thank you for playing! The parrot was " , parrot_age , " years old")

