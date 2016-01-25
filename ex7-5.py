# -*- coding: cp1252 -*-
import math

print("Calculator")

a = int(input("Give the first number: "))
b = int(input("Give the second number: "))



while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7) Change numbers\n(8) Quit\nCurrent numbers: ", a, b)
    choice = int(input("Please select something (1-8): "))

    if(choice == 1):
        result = a + b
        print("The result is:", result)
    elif(choice == 2):
        result = a - b
        print("The result is:", result)
    elif(choice == 3):
        result = a * b
        print("The result is:", result)
    elif(choice == 4):
        result = a / b
        print("The result is:", result)
    elif(choice == 5):
        result = math.sin(a/b)
        print("The result is:", result)
    elif(choice == 6):
        result = math.cos(a/b)
        print("The result is:", result)
    elif(choice == 7):
        a = int(input("Give the first number: "))
        b = int(input("Give the second number: "))
    elif(choice == 8):
        print("Thank you!")
        break
    else:
        print("Selection was not correct.")

