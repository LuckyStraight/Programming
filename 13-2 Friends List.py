#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Friends list
#
# Filename:     13-1
# Date:  11/17/2021
#-------------------------------------------------------------------------------

while True:
    name = input("enter in a name:")
    if name == "": # must hit enter to break the prompt of asking for name
        break
    name += "\n" # creates a space inbetween each name entered

    file = open("friends.txt", "a") # creates a text file to hold the names
    file.write(name)
    file.close

file = open("friends.txt", "r") # Reads the inputed names in the text file to be shown
for i in file:
    print(i,end="")

