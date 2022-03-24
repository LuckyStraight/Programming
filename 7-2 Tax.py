#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     tax
#
# Filename:     7-2
# Date:  9/30/2021
#--------------------------------------------------------------------------------

def main():
    lot_number = -1
    while lot_number != 0:
        lot_number = int(input("what is the lot number?:"))
        if lot_number == 0: # if input is 0 it will stop the loop
            break
        show_tax()

# this does the calculations for the property tax
def show_tax():
    property_value = int(input("What is property value?:"))
    property_tax = property_value *0.0065
    print("enter the properties lot or 0 to end:")
    print("proteries tax is $:", property_tax)

main()