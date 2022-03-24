#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     numbers quiz
#
# Filename:     7-1
# Date:  9/30/2021
#--------------------------------------------------------------------------------

import random 
rng = random.Random()
number = rng.randrange(1, 20) #creates random numbers between 1-20
cancel = "n"
guesses = 0
msg =""

#creates random addition problem
def randomnummers():
    x = random.randrange(20) + 1
    y = random.randrange(20) + 1
    print("what is", x, "+", y, "?")
    return x + y

while cancel =="n":
    number = randomnummers()

    while True:
        guess = int(input(msg + "\nGuess the solution to x + y: ")) # creates the problem
        guesses += 1
        if guess > number:
            msg += str(guess) + " is too high.\n" # lets the guesser know the value is too high
        elif guess < number:
            msg += str(guess) + " is too low.\n" #Lets the guesser know the value is too low
        else:
            break

    cancel = input("would you like to stop, Y or N:") #stops the loop if they answer no
    cancel = cancel.lower()
    

print("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses)) # keeps track of the number of guesses it took

