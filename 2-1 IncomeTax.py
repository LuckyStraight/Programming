#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     calculating income tax
#
# Filename:     2-1
# Date:  8/24/2021
#-------------------------------------------------------------------------------
tax_rate = .20
standard_deduction = 10000.0
deduction_per_dependent = 3000.000

gross_income = float(input("gross income: "))
dependents = int(input("dependents: "))

net_income = gross_income - standard_deduction - dependents * deduction_per_dependent

print(net_income * tax_rate)
