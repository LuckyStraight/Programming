#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Sally Seashore Supplies
#
# Filename:     7-5
# Date:  10/6/2021
#--------------------------------------------------------------------------------
#Sammy's logo
def display():
    print("""
##############################################
$                                            $
$    SAMMY'S MAKES FUN IN THE SUN            $
$                                            $
$                                            $
##############################################
""")
#display the minutes rented and store in variable
def getinput(): #contract number and rental time
    account_number = input("account number:")
    minutes = int(input("the amount of minutes rented: "))
    while minutes < 60 or minutes > 7200:
        minutes = int(input("the amount of minutes rented: "))
    return account_number, minutes

#calculate number of whole hours, number of minutes remaining, cost as hours * 40 + minutes remaining times 1
def calculate_total(account_number,minutes):
    hours = minutes // 60         #calculate number of whole hours
    minutes_remaining = minutes % 60    #calculate the number of minutes remaining
    

    if minutes_remaining > 40:
        hours = hours + 1
        minutes_remaining = 0
        
   
    rental_cost = hours * 40 + minutes_remaining *1       #calculate the cost as hours * 40 + minutes remaining times 1
    hours = minutes // 60         #calculate number of whole hours
    minutes_remaining = minutes % 60    #calculate the number of minutes remaining

    print("ACCOUNT NUMBERS:", account_number)     #display minutes, whole hours, minutes remaining and cost with lables
    print("minutes rented:", minutes)
    print("whole hours rented:", hours)
    print("minutes remaining:", minutes_remaining)
    print("rental cost: $", rental_cost)
    count = 0
    while hours > count:
        print("Coupon good for 10 percent off next rental" )
        count += 1


def main():
    display()
    account_number, minutes = getinput()
    calculate_total(account_number, minutes) 

main()