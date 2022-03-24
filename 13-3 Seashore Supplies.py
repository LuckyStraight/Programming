#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Sallys seashore Supplies
#
# Filename:     13-3
# Date:  11/17/2021
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

    supplies = ["kayak", "canoe", "chairs", "umbrella"]
    while True:
        Rental = input("enter in a product kayak, canoe, chairs, umbrella:")
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

    for item in (account_number, minutes,phone_num,fname,lname,Rental): # shows these items in the text file
        order.append(item)

    thisorder = ""

    for i in order:
        thisorder += str(i) + " "

    thisorder += "\n"
    file = open("order.txt", "a") # creates a text file order
    file.write(thisorder)
    file.close()



#calculate number of whole hours, number of minutes remaining, cost as hours * 40 + minutes remaining times 1
def calculate_total():
    file = open("order.txt", "r") # reads the text file order that was created
    orders = []

    for line in file:
        orders.append(line)

    for val, i in enumerate(orders): # Helps with placing a space in between each item.
        orders[val] = i.split()

    for order in orders: #has the prices and the minutes remaining cost for each of the products
        kayak =  [60, 5]
        canoe = [50,4]
        chairs = [10,1]
        umbrella = [5,.50]
        price = 0

        # Calls the prices of the products to be used
        if order[5] == "kayak":
            price = kayak
        if order[5] == "canoe":
            price = canoe
        if order[5] == "chairs":
            price = chairs
        if order[5] == "umbrella":
            price = umbrella

        hours = int(order[1]) // 60 #calculate number of whole hours
        minutes_remaining = int(order[1])% 60 #calculate the number of minutes remaining
        

        if minutes_remaining > price[0]/price[1]:
            hours = hours + 1
            minutes_remaining = 0

        rental_cost = hours * price[0] + minutes_remaining *price[1] #calculate the cost as hours * 40 + minutes remaining times 1
        hours = int(order[1]) // 60  #calculate number of whole hours
        minutes_remaining = int(order[1]) % 60  #calculate the number of minutes remaining

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
    choice = input("enter in a number: 1 Add new order and save to disk, 2 Print all orders, 3 quite")
    if choice == "1":
        getinput()
    if  choice == "2":
        calculate_total() 
    if choice == "3":
        exit

main()