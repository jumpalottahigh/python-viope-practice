mynumber = input("Give a number: ")
try:
    mynumber = int(mynumber)
    print("The input was suitable!")
except Exception:
   print("The input was malformed.")