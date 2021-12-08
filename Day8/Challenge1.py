# AoC 2021 Day 8
# Challenge 15/50
# Answer 392

import sys
import os
import math
from statistics import mean

input = []
signals = []
digits = []

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
   lines = f.readlines()
   for line in lines:
       input.append(line.strip())

outputCount = 0

for l in input:
    s, d = l.split(' | ')
    signals.append(s)
    digits.append(d)

signals = list(map(str.split, signals))
digits = list(map(str.split, digits))

for index in range( len(signals)):
    for s in signals[index]:
        signalSize = len(s)
        if signalSize == 2 or signalSize == 3 or signalSize == 4 or signalSize == 7:
            for di in range( len(digits[index]) ):
                digitSize = len(digits[index][di])
                if signalSize == digitSize:
                    outputCount+=1

print(outputCount)
