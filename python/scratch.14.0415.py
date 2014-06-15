import random

def sim(size):
    count = 0
    digits = []
    for i in range(size):
        digits.append(i)
    l = []
    while l != digits:
        l = []
        for i in range(len(digits)):
            l.append(int(random.random()*len(digits)))
        l.sort()
        count += 1
    return count

rawsum = 0
simcount = eval(input("Simulation count: "))
for i in range(simcount):    
    rawsum += sim(simcount)
print("Average:", rawsum/simcount)
