# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Learn and apply exception handling and pickling module in a Python.
# ChangeLog (Who,When,What):
# CPark,2.25.2022,Started and finished code for assignment 7.
# CPark,2.26.2022,Added comments
# ---------------------------------------------------------------------------- #

import pickle

strName = ""
intPhone = ""
lstContact = []
objFile = ""

# Beginning a while loop and ask user if they want to add new contact
while (True):
    strChoice = input("Would you like to add a new contact? (Yes/No) ")
    print("")
    # If user answers yes, then asks for name and phone number
    if strChoice.lower() == "yes":
        print("Great, let's add a contact")
        try:
            strName = str(input("Name: "))
            intPhone = int(input("Phone Number: "))
            print("")
            # Start a .dat file and add contact information using pickle.dump
            lstContact = [strName, intPhone]
            objFile = open("contact.dat","ab")
            pickle.dump(lstContact, objFile)
            objFile.close()
        # If error occurs then print an error message
        except:
            print("ERROR: Please enter a valid number")
    else:
        print("Viewing contacts...")
        break

# pickle.load contact.dat and print to user
# whileloop to print all contacts added rather than first row
objFile = open("contact.dat","rb")
while(True):
    try:
        objContact = pickle.load(objFile)
        print(objContact)
    except:
        print("")
        print("Good bye")
        break
objFile.close