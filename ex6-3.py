# -*- coding: cp1252 -*-

def main():
    while True:
        userinput = input("Write something (quit ends): ")
        if(userinput == "quit"):
            break
        else:
            tester(userinput)

def tester(givenstring="Too short"):
    if(len(givenstring) < 10):
        print("Too short")
    else:
        print(givenstring)


if __name__ == "__main__":
    main()