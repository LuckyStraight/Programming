#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     loops and lists
#
# Filename:     3-1
# Date:  9/1/2021
#-------------------------------------------------------------------------------

# The number in the list
xs = [12, 10, 32, 3, 17, 20]

print("The numbers in the list")

for i in xs:
    print(i)

# The numbers squared
print("\nThe numbers squared")

for i in xs:
    print(i, i ** 2)

# The numbers total
total = 0
for i in xs:
    total += i
print("\nTotal:", total)

# The numbers product
product = 1
for i in xs:
    product *= i
print("\nProduct for all numbers", product)








