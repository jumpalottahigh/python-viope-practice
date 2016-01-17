# -*- coding: cp1252 -*-

readfile = open("facts.txt", "r")
content = readfile.readlines()
print("Following was read from the file: ")

for i in content:
    print(i)

readfile.close()