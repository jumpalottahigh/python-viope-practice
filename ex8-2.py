def openf():
    fname=input("Give the file name: ")
    try:
        handler = open(fname, 'r')
        content = handler.read()
        handler.close()
        return content
    except IOError:
        return False

def conversion(fcontent):
    try:
        fcontent=int(fcontent)
        return fcontent
    except Exception:
        return False

def main():
    result=openf()
    if result == False:
        print("There seems to be no file with that name.")
    elif conversion(result) == False:
        print("The file contents were unsuitable.")
    else:
        print("The result was", 1000/conversion(result))

if __name__=="__main__":
    main()