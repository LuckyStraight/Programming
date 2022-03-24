#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     moon bucks
#
# Filename:     5-4
# Date:  9/23/2021
#--------------------------------------------------------------------------------

#defines the price of the sizes
def calculate_display(cs, r):
    if cs == "S" or cs == "s":
        price = 2.95
    elif cs == "M" or cs == "m":
        price = 3.50
    elif cs == "L" or cs == "l":
        price = 4.05

    #calculates the tax and subtotal
    tax = price * .06
    subtotal = price + tax

#This is if the customer is a Rewards member to get a discount
    if r == "y" or r == "Y":
        r = price * .2
        print("your bill:")
        print("price:", round(price,2))
        print("tax:", round(tax,2))
        print("subtotal:", round(subtotal,2))
        print("discount:", round(r,2))
        print("===============")

#This is if the customer isn't a Rewards member and gets no discount
    elif r =="n" or r == "N":
        print("your bill:")
        print("price:", round(price,2))
        print("tax:", round(tax,2))
        print("subtotal:", round(subtotal,2))
        print("no discount: scrub")
        print("===============")

#calculates the total (doesn't change so doesn't need to be in if statements)
    total = subtotal - r
    print("total:", round(total,2))

#Defining the size and if they're a rewards member
def main():
    coffee_size = input("S,M or L")
    rewards = input("Are you a Rewards Members? Y or N?")
    coffee_size = coffee_size.lower()
    rewards = rewards.lower()

    calculate_display(coffee_size,rewards)

main()


