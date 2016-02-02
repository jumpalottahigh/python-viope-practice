note = []
while True:

    try:
        userchoice = int(input("Would you like to \n(1)Add or \n(2)Remove items or\n(3)Quit?:"))
    except Exception:
        print("Incorrect input: Enter a number")

    if userchoice == 'end':
        break
    elif userchoice == 1:
        note.append(input("What will be added?: "))
    elif userchoice == 2:
        print("There are", len(note),"items in the list.")
        itemToDelete=int(input("Which item is deleted?: "))
        try:
            note.pop(itemToDelete)
        except Exception:
            print("Incorrect selection.")
    elif userchoice == 3:
        print("The following items remain in the list:")
        for i in note:
            print(i)
        break
    else:
        print("Incorrect selection.")