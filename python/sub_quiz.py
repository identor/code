import time
import random

QUESTION_COUNT = 5
QUESTION_MIN = 0
QUESTION_MAX = 10

start = time.time()
correct_count = 0
counter = 0

while counter < QUESTION_COUNT:
    minuend = random.randint(QUESTION_MIN, QUESTION_MAX)
    subtrahend = random.randint(QUESTION_MIN, QUESTION_MAX)
    
    if minuend < subtrahend:
        minuend, subtrahend = subtrahend, minuend # swap values

    answer = eval(input("What is " + str(minuend)
                        + " - " + str(subtrahend) + "?: "))
    # correct_count += 1 if minuend - subtrahend == answer else 0
    if minuend - subtrahend == answer:
        correct_count += 1
    else:
        print("Answer is incorrect")
        
    counter += 1
    
total_time = time.time() - start
print("Correct answers:", correct_count, "out of", QUESTION_COUNT)
print("Time taken to finish: ", format(total_time, ".2f"), "seconds")
input("Press Enter to continue...")
