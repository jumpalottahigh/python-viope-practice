# -*- coding: cp1252 -*-

#The idea is to create a program which asks for a user name and password.
# If the given name is wrong, the program prints "The given name is wrong".
# If the name is acceptable, the program asks for the password.
# If the password is correct, the system prints "Both inputs are correct!", otherwise "The password is incorrect.".
# The correct inputs should be "John" and the password "ABC123". Overall, the program should print the following:

user = input("Give name: ")

if(user == "John"):
    user = input("Give password: ")
    if(user == "ABC123"):
        print("Both inputs are correct!")
    else:
        print("The password is incorrect.")
else:
    print("The given name is wrong.")

