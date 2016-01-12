# -*- coding: cp1252 -*-

print("Calculator")

a = int(input("Give the first number: "))
b = int(input("Give the second number: "))

print("(1) +\n(2) -\n(3) *\n(4) /")

choice = int(input("Please select something (1-4): "))

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
else:
    print("Selection was not correct.")

