f = open("cat_with_flag.txt", "r")

i = 0
str = ""
letters = 0

for char in f.read():
    if char == "\n":
        i -= 1

    if i%9 == 7:
        str += char
        letters += 1
    if i%72 == 1:
        str += " "

    i += 1

    if letters > 400:
        break




print(str)


f.close()

print("hi")