question1 = "Is your birthday in Set1? \n" + \
            "     1   3   5   7 \n" + \
            "     9  11  13  15 \n" + \
            "    17  19  21  23 \n" + \
            "    25  27  29  31 \n" + \
            "yes or no <y/n>:"

question2 = "Is your birthday in set2? \n" + \
            "     2   3   6   7 \n" + \
            "    10  11  14  15 \n" + \
            "    18  19  22  23 \n" + \
            "    26  27  30  31 \n" + \
            "yes or no <y/n>:"

question3 = "Is your birthday in set3? \n" + \
            "     4   5   6   7 \n" + \
            "    12  13  14  15 \n" + \
            "    20  21  22  23 \n" + \
            "    28  29  30  31 \n" + \
            "yes or no <y/n>:"

question4 = "Is your birthday in set4? \n" + \
            "     8   9  10  11 \n" + \
            "    12  13  14  15 \n" + \
            "    24  25  26  27 \n" + \
            "    28  29  30  31 \n" + \
            "yes or no <y/n>:"

question5 = "Is your birthday in set5? \n" + \
            "    16  17  18  19 \n" + \
            "    20  21  22  23 \n" + \
            "    24  25  26  27 \n" + \
            "    28  29  30  31 \n" + \
            "yes or no <y/n>:"

birthday = 0

if input(question1) == 'y':
    birthday += 1

print()
if input(question2) == 'y':
    birthday += 2

print()
if input(question3) == 'y':
    birthday += 4

print()
if input(question4) == 'y':
    birthday += 8

print()
if input(question5) == 'y':
    birthday += 16

print("\nYour birthday is", birthday)
input("Press Enter to continue...")
