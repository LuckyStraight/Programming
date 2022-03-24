#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     FiveStar
#
# Filename:     2-3
# Date:  8/24/2021
#-------------------------------------------------------------------------------

#intital constants
new_rental = 3.00
old_rental = 2.00

#request the inputs
new_vids = int(input("number of New rentals: "))
old_vids = int(input("number of old rentals: "))
#compute the results
total_cost = new_rental * new_vids + old_rental * old_vids

#display the results
print("$", total_cost)