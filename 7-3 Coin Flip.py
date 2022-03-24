#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     coin flip
#
# Filename:     7-3
# Date:  9/30/2021
#--------------------------------------------------------------------------------

import random 
def main ():
    rng = random.Random()
    number = rng.randrange(1, 2)
    heads = 0 #starting value of heads before code runs
    tails = 0 #starting value of tails before code runs

    for i in range(1000):
        number = random.randrange(2)+1 #generate code between 1 and 2
        x = 1
        y = 2
        if number == x: #calcualtes the number of heads that was flipped
            heads += 1
        else:
            tails += 1  #calcualtes the number of tails that was flipped



    print("you had", heads, "heads and", tails, "tails") #tells how many heads and tails have happened

main()