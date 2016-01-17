# -*- coding: cp1252 -*-

def main():
    while True:
        userinput = input("Write something (quit ends): ")
        if(userinput == "quit"):
            break
        else:
            if(tester(userinput)):
                print("X spotted!")
            else:
                if((len(userinput) > 10)):
                    print(userinput)

def tester(givenstring="Too short"):
    if(len(givenstring) < 10):
        print("Too short")
        return False
    else:
        for i in givenstring:
            if i == "X":
                print(givenstring)
                return True
        else:
            return False

if __name__ == "__main__":
    main()