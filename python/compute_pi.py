from random import random
import math

TRIAL_MAX_COUNT = 10000000
hit_count = 0
radius = 1

print("Calculation Vaule of PI...")
for i in range(TRIAL_MAX_COUNT):
    x = random()*2 - 1
    y = random()*2 - 1
    
    if x*x + y*y <= radius:
        hit_count += 1

pi = hit_count/TRIAL_MAX_COUNT * 4
print("Approximated value of pi:", pi)
input("Press Enter to continue...")
