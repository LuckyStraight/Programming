#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Functions
#
# Filename:     5-3
# Date:  9/23/2021
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
    c = int(input("1) add, 2) sub, 3) mul, 4) div"))
    if c == 1:
        print("sum:", add(a,b))
    if c == 2:
        print("sub:", sub(a,b))
    if c == 3:
        print("mul:", mul(a,b))
    if c == 4:
        if b == 0:
            print("division by 0 is not allowed, THAT'S ILLEGAL!!!!!")
        else:
            print("div:", div(a,b))
    

main()
