# print header
print(format("Multiplication Table", "^40s"))

for i in range(10):
    for j in range(10):
        if i == 0:
            if j == 0: print(format("", "4s"), end='')
            else: print(format(j, "4d"), end='')
        else:
            if j == 0: print(format(str(i)+'|', ">4s"), end='')
            else: print(format(i*j, "4d"), end='')
    print()
    if i == 0: print(format('', "->40s"))
input("Press Enter to continue...")
