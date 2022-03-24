#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     products
#
# Filename:     11-2
# Date:  11/3/2021
#-------------------------------------------------------------------------------

def product(ls1,ls2):
    total = ""
    for i in range(len(ls1)):
        total += str(ls1[i] * ls2[i]) +"," # multiples the lists together
        

    print(total)


def main(): # holds the lists
    list1 = [3,7,9,3,2, 8]
    list2 = [5,8,2, 5, 20, 16] 
    product(list1,list2)

main()

