#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     Data Form
#
# Filename:     8-2
# Date:  10/13/2021
#--------------------------------------------------------------------------------

import string

while True: #asks for the first name of user
    fname = input("first name:")
    if fname.isalpha():
        break


while True: #asks for the last name of user
    lname = input("last name:")
    if fname.isalpha():
        break


while True: #asks for the phone number of user
    phone_num = input("Phone number:")
    if len(phone_num)== 7 and phone_num.isdigit(): #makes sure the phone number is equal to 7 digits
        break
phone_num = phone_num[0:3] + "-" + phone_num[3:7] #inserts hyphen after first 3 number in the phone number


while True: #asks for the social security number of user
    social_security = input("social security:")
    if len(social_security)==9 and social_security.isdigit(): #makes sure the social security number is equal to 9 digits
        break

while True: #asks for the zip code of user
    zip = input("enter in your zip code:")
    if len(zip)==5 and zip.isdigit(): #makes sure the zip code is equal to 5 digits
        break

while True: #asks for the email address of user
    email = input("enter email address:")
    if "@" in email and "." in email: #makes sure that the email address has an @ and period
        break

print("sally's internet sales")
print("first name:", fname)
print("last name:", lname)
print("phone number:", phone_num)
print("social security:", social_security)
print("zip code:", zip)
print("email address:", email)

