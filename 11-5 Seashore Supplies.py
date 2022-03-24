#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Sally seashore Supplies
#
# Filename:     11-5
# Date:  11/16/2021
#-------------------------------------------------------------------------------

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
    order = []
    fname = input("first name:")
    lname = input("last name:")

    supplies = ["kayak", "canoe", "beach_chairs", "umbrella"]
    while True:
        Rental = input("enter in a product kayak, canoe, beach_chairs, umbrella:")
        if Rental in supplies:
            break


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
    for item in (account_number, minutes,phone_num,fname,lname,Rental):
        order.append(item)
    return order

#calculate number of whole hours, number of minutes remaining, cost as hours * 40 + minutes remaining times 1
def calculate_total(order):
    kayak =  [60, 5]
    canoe = [50,4]
    beach_chairs = [10,1]
    umbrella = [5,.50]
    price = 0

    if order[5] == "kayak":
        price = kayak
    if order[5] == "canoe":
        price = canoe
    if order[5] == "beach_chairs":
        price = beach_chairs
    if order[5] == "umbrella":
        price = umbrella

    hours = order[1] // 60 #calculate number of whole hours
    minutes_remaining = order[1] % 60 #calculate the number of minutes remaining
    

    if minutes_remaining > price[0]/price[1]:
        hours = hours + 1
        minutes_remaining = 0

    rental_cost = hours * price[0] + minutes_remaining *price[1] #calculate the cost as hours * 40 + minutes remaining times 1
    hours = order[1] // 60  #calculate number of whole hours
    minutes_remaining = order[1] % 60  #calculate the number of minutes remaining

    if minutes_remaining > price[0]:
        minutes_remaining = price[0]

    print("ACCOUNT NUMBERS:", order[0]) #display minutes, whole hours, minutes remaining, cost, phone number, first and last name with lables
    print("name:",order[3],order[4])
    print("phone number:", order[2])
    print("minutes rented:", order[1])
    print("whole hours rented:", hours)
    print("minutes remaining:", minutes_remaining)
    print("rental cost: $", rental_cost)
    count = 0
    while hours > count:
        print("Coupon good for 10 percent off next rental" )
        count += 1


def main():
    display()
    order = getinput() #calls variables to the main function
    calculate_total(order) 

main()