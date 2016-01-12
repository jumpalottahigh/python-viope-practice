# -*- coding: cp1252 -*-

#The third exercise is to create a conditional structure which prints a line depending on the given selection.
# The program asks a number between 1 and 3, and based on the number prints the following:
#  1 prints "You selected one.", 2 prints "You selected two." and 3 prints "You selected three.", like this:

user = int(input("Select a number (1-3): "))

if(user == 1):
    print("You selected one.")
elif(user == 2):
    print("You selected two.")
elif(user == 3):
    print("You selected three.")
else:
    print("You selected something else.")

