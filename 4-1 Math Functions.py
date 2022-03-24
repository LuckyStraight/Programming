#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Four Functions
#
# Filename:     4-1
# Date:  9/7/2021
#--------------------------------------------------------------------------------

#function to add
def add(a,b):
    return a + b

#function to subtract
def sub(a,b):
    return a - b

#function to multiply
def mul(a,b):
    return a * b

#function to divide
def div(a,b):
    return a / b

#function to handle interaction with user
def main():
    a = int(input("enter in a"))
    b = int(input("enter in b"))
    print("Sum: 5 + 4 =",add(a,b))
    print("Difference: 5 - 4 =",sub(a,b))
    print("Product: 5 * 4 =",mul(a,b))
    print("Quotient: 5 divided by 4 =",div(a,b))

main()
