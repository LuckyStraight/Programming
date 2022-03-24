#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Encapsulate
#
# Filename:     8-3
# Date:  10/19/2021
#--------------------------------------------------------------------------------

def count_letters(p,let): #counts the specfic letter the use entered from the phrase
    count = 0
    for i in p:
        if i == let:
            count += 1
    return count

def main():
    phrase = input("enter in a sentence:") #enters in users phrase
    letter = input("what letter are we looking for:") #enters in users letter choice
    letter_count = count_letters(phrase,letter) #calls the count letter function to the main
    print("there are", letter_count, "occurences of", letter, "in", phrase)

main()