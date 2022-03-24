#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     phone book
#
# Filename:     11-1
# Date:  11/3/2021
#-------------------------------------------------------------------------------

name_list = []
number_list = []
num = 0

def phonebook():
    global num
    while True:
        name = input("enter a name:") # entering a name
        phone_num = input("enter a number:") # entering a number

        name_list.append(name) #stores the name(s)
        number_list.append(phone_num) #stores the number(s)
        num += 1
        if name == "": #hit enter for the name and number to stop the loop
            return name_list, number_list



def printbook(nalist,nulist):
    print("\nName\t\t\tPhone Number\n")

    for i in range(num):
        print("{}\t\t\t{}". format(name_list[i], number_list[i])) #prints the list of names and numbers



def searchfor(nalist,nulist):
    search_term = input("\nEnter search term:")
    print("Search result:")

    if search_term in name_list: # searches the inputed name and corresponding phone number
        index = name_list.index(search_term)
        phone_num = number_list[index]
        print("Name; {}, Phone Number: {}".format(search_term, phone_num))
    else: # displays this if inputed name or number not found
        print("Name Not Found")

def main(): # calls the function 
    na, nu= phonebook()
    printbook(na,nu)
    searchfor(na,nu)

main()



