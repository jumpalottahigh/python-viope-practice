import pickle
import time

'''
Helpers
'''

def readfile(fname):
    while True:
        try:
            handle = open(fname,'rb')
            content = pickle.load(handle)
            handle.close()
            return content
        except IOError:
            newfile(fname)
            print("No default notebook was found, created one.")

def writefile(note, fname):
    try:
        writefile = open(fname, 'wb')
        pickle.dump(note, writefile)
        writefile.close()
    except IOError:
        return False

def newfile(fname):
    try:
        newfile = open(fname,'wb')
        note=[]
        pickle.dump(note, newfile)
        newfile.close()
    except IOError:
        return False

def editnote(note):
    print("The list has", len(note),"notes.")
    try:
        noteToEdit = int(input("Which of them will be changed?:"))
        print(note[noteToEdit])
        newNote = input("Give the new note: ")
        newNote = newNote+":::"
        newNote += time.strftime("%X %x")
        note[noteToEdit] = newNote
        return note
    except Exception:
        print("Incorrect value.")

def deletenote(note):
    print("The list has", len(note),"notes.")
    try:
        noteToDel = int(input("Which of them will be deleted?: "))
        noteToDel -= 1
        print("Deleted note", note[noteToDel])
        note.pop(noteToDel)

        return note
    except Exception:
        print("Incorrect value.")

def main():
    note = []
    fname = "notebook.dat"
    note = readfile(fname)
    while True:
        userchoice=input('''(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit
Please select one: ''')
        if userchoice == '1':
            for i in note:
                print(i)
        elif userchoice == '2':
            newNote=input("Write a new note: ")
            newNote = newNote+":::"
            newNote += time.strftime("%X %x")
            note.append(newNote)
        elif userchoice == '3':
            note = editnote(note)
        elif userchoice == '4':
            note = deletenote(note)
        elif userchoice == '5':
            writefile(note, fname)
            print("Notebook shutting down, thank you.")
            break

if __name__ == "__main__":
    main()