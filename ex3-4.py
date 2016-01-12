# -*- coding: cp1252 -*-

#The third exercise is to create a conditional structure which prints a line depending on the given selection.
# The program asks a number between 1 and 3, and based on the number prints the following:
#  1 prints "You selected one.", 2 prints "You selected two." and 3 prints "You selected three.", like this:

n1 = int(input("Give a number: "))
n2 = int(input("Give another number: "))

if(n1 % 2 == 0 and n2 % 2 == 0):
    print("Both numbers are even.")
elif(n1 % 2 == 0 or n2 % 2 == 0):
    print("One of the numbers is even.")
else:
    print("Both numbers are odd.")

