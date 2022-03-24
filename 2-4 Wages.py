#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     employee pay
#
# Filename:     2-4
# Date:  8/24/2021
#-------------------------------------------------------------------------------

#request the inputs
wage = int(input("hourly wage: $"))
hours = int(input("regular hours: "))
overtime_hours = int(input("overtime hours: "))

#compute the results
overtime_pay = overtime_hours * 1.5 * wage
weekly_pay = wage * hours + overtime_pay

#display the results
print("$", weekly_pay)
