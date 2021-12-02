# AoC 2021 Day 1
# Challenge 1
# Answer 1316
depths = []

with open(r'C:\Users\jerem\Documents\Projects\AoC2021\Day1\Input.txt') as f:
   lines = f.readlines()
   for line in lines:
      depths.append(int(line.strip()))

prev = depths[0]
desendCount = 0
for i in depths:
    if i > prev:
        desendCount+=1
    prev = i

print( desendCount )