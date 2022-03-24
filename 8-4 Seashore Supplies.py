#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Sammy’s Seashore Supplies
#
# Filename:     8-4
# Date:  10/19/2021
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
    fname = input("first name:")
    lname = input("last name:")

    account_number = input("account number:")
    while "a" != account_number [0] and len(account_number)!= 4: #checks to see if the account number starts with a and has 4 digits
        account_number = input("account number:") #prompts the user for account number again if first prompt didn't start with a

    while True: #asks for the phone number of user
        phone_num = input("Phone number:")
        if len(phone_num)== 7 and phone_num.isdigit(): #makes sure the phone number is equal to 7 digits
            break
    phone_num = phone_num[0:3] + "-" + phone_num[3:7] #inserts hyphen after first 3 number in the phone number

    minutes = int(input("the amount of minutes rented: "))
    while minutes < 60 or minutes > 7200:
        minutes = int(input("the amount of minutes rented: "))
    return account_number, minutes,phone_num,fname,lname

#calculate number of whole hours, number of minutes remaining, cost as hours * 40 + minutes remaining times 1
def calculate_total(account_number, minutes,phone_num,fname,lname):
    hours = minutes // 60         #calculate number of whole hours
    minutes_remaining = minutes % 60    #calculate the number of minutes remaining
    

    if minutes_remaining > 40:
        hours = hours + 1
        minutes_remaining = 0
        
   
    rental_cost = hours * 40 + minutes_remaining *1       #calculate the cost as hours * 40 + minutes remaining times 1
    hours = minutes // 60         #calculate number of whole hours
    minutes_remaining = minutes % 60    #calculate the number of minutes remaining

    print("ACCOUNT NUMBERS:", account_number)     #display minutes, whole hours, minutes remaining, cost, phone number, first and last name with lables
    print("name:",fname,lname)
    print("phone number:", phone_num)
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
    account_number, minutes,phone_num,fname,lname = getinput() #calls variables to the main function
    calculate_total(account_number, minutes,phone_num,fname,lname) 

main()