DISPLAY_MAX = 50
PER_LINE_MAX = 10

count = 0
dividend = 2 # prime numbers are greater than one

print("The first 50 prime numbers are: ")

while count < DISPLAY_MAX:
    isPrime = True

    divisor = 2
    while divisor <= dividend/2:
        if dividend % divisor == 0:
            isPrime = False
            break
        divisor += 1

    if isPrime:
        count += 1

        print(format(dividend, "4d"), end='')
        if count % PER_LINE_MAX == 0:
            print()

    dividend += 1
input("Press Enter to continue...")
