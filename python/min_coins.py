amount = eval(input("Enter an amount: "))

cents = int(amount * 100) # drop decimal

quarters = cents // 25
cents -= quarters * 25

dimes = cents // 10
cents -= dimes * 10

nickels = cents // 5
cents -= nickels * 5

pennies = cents

print("Quarters:", quarters, "Dimes:", dimes, "Nickels", nickels,\
      "Pennies:", pennies)

input("Press Enter to continue...")
