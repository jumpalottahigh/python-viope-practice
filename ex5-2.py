# -*- coding: cp1252 -*-

fname = input("Give a file name: ")

ftext = input("Write something: ")

handle = open(fname, "w")
handle.write(ftext)
handle.close()

print("Wrote", ftext, "to the file", fname)