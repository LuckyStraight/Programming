#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     number quiz
#
# Filename:     5-2
# Date:  9/21/2021
#-------------------------------------------------------------------------------

import random

#creates random addition problem
def randomnummers():
    x = random.randrange(20) + 1
    y = random.randrange(20) + 1
    print("what is", x, "+", y, "?")
    return x + y

#defines the guessed number the user chose
def main():
    solution = randomnummers()
    guess = int(input("guess nummer now"))

#if the solution is correct
    if guess == solution:
        print("you is correct!")
        print("you is smart smart")

#if the solution was incorrect
    else:
        print(solution)
        print("you is dumb!")
        print("you are loser!")

main()


