fname = "words.txt"

try:
    handle = open(fname,"r")
    words = []
    while True:
        content = handle.readline()
        if content == "":
            break
        else:
            words.append(content)
    handle.close()
except IOError:
    print("No such file!")

words.sort()

print("Words in an alphabetical order:")
for i in words:
    print(i)