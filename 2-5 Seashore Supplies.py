#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     sammy's seashore supplies
#
# Filename:     2-5
# Date:  8/26/2021
#-------------------------------------------------------------------------------
#Sammy's logo
print("""
##############################################
$                                            $
$    SAMMY'S MAKES FUN IN THE SUN            $
$                                            $
$                                            $
##############################################
""")
#display the minutes rented and store in variable
minutes = int(input("the amount of minutes rented: "))

#calculate number of whole hours
hours = minutes // 60

#calculate the number of minutes remaining
minutes_remaining = minutes % 60

#calculate the cost as hours * 40 + minutes remaining times 1
rental_cost = hours * 40 + minutes_remaining *1

#display minutes, whole hours, minutes remaining and cost with lables
print("minutes rented:", minutes)
print("whole hours rented:", hours)
print("minutes remaining:", minutes_remaining)
print("rental cost:", rental_cost)


