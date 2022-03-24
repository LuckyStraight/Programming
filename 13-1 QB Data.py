#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     QBData
#
# Filename:     13-1
# Date:  11/17/2021
#-------------------------------------------------------------------------------

infile = open("qbdata.txt", "r") # calls the text file to be used
linelist = infile.readlines()

for line in linelist:
    if float(line.split()[10]) >= 90: #searches for names with ratings over 90%
        print(line.split()[0], line.split()[1], "\t", line.split()[3], "\t", line.split()[10], "%") #prints the first and last name, position, and rating of the player



