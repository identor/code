import random

number = random.randint(0, 100)

print("Guess a magic number between 0 and 100.")
guess = eval(input("Enter your guess: "))

while guess != number:
    print("Your guess is too high" if guess > number
          else "Your guess is too low")
    guess = eval(input("Enter your guess: "))

print("Yes the number is", number)
input("Press Enter to continue...")
