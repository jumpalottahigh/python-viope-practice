while True:
    fname = input("Give the file name: ")

    try:
        file = open(fname, "r")
    except:
        print("There seems to be no file with that name.")
        continue
    else:
         print("The result was",result)