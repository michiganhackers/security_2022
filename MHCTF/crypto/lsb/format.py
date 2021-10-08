f = open("cool_cat_binary.txt", "r")
f_out = open("cool_cat_binary_out.txt", "a")

i = 0

for char in f.read():
    f_out.write(char)

    if char == " ":
        i += 1

    if i%8 == 0:
        f_out.write("\n")
        i+= 1


f.close()
f_out.close()

print("hi")