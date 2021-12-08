# AoC 2021 Day 7
# Challenge 13+14/50
# Answer 352707 / 95519693

import sys
import os
import math
from statistics import mean

def align(_target, _prevBest ):
    tCrabs = crabs.copy()
    fuel = 0
    done = False
    step = 1
    while done == False:
        done = True
        for crab in range(len(tCrabs)):
            if tCrabs[crab]<_target:
                done=False
                tCrabs[crab]+=1
                fuel+=step
            elif tCrabs[crab]>_target:
                done=False
                tCrabs[crab]-=1
                fuel+=step

            if fuel >= _prevBest:
                return fuel

        #challenge 2    
        step += 1
    return fuel

input =[]
crabs = []

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
   lines = f.readlines()
   for line in lines:
       input.append(line.strip())

input = input[0].split(',')
crabs = list(map(int, input))

crabs.sort()

avg = math.floor(mean(crabs))
target = avg
bestTarget = target
fuel = align(target, sys.maxsize)
print("Predict Answer %d" % fuel)

for index in range( max(crabs) ):

    nFuel = align( target, fuel )
    if nFuel < fuel:
        bestTarget = target
        fuel = nFuel
    target+=1
    sys.stdout.write("Fuel [%d]-%d : %d - %d       \r" % ( fuel, nFuel, target, bestTarget))

sys.stdout.write("\n\r")
print("Answer %d" % fuel)


