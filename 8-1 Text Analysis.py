#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Text Analysis
#
# Filename:     8-1
# Date:  10/13/2021
#--------------------------------------------------------------------------------

#this removes all forms of punctutation in any sentence
import string
def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def main():
    ss = input("enter in a phrase:")
    new = remove_punctuation(ss)
    print(new)

    words = new.split(" ") #splits the words in the sentence
    e = 0
    for i in words: #counts the number of e that is present in the sentence
        if "e" in i:
            e +=1

    percentage = e/len(words) * 100 #calculates the percentage of e in the sentence

    print(words,"the percentage of e:",percentage, "%")

main()



