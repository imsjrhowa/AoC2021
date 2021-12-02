# AoC 2021 Day 1
# Challenge 2
# Answer 1344
depths = []

with open(r'C:\Users\jerem\Documents\Projects\AoC2021\Day1\Input.txt') as f:
   lines = f.readlines()
   for line in lines:
      depths.append(int(line.strip()))

prev = depths[0]+depths[1]+depths[2]
desendCount = 0

size = len(depths)

for i in range(size):

    if i >= size or i+1 >= size or i+2 >= size:
        break

    v1 = depths[i]
    v2 = depths[i+1]
    v3 = depths[i+2]

    if v1+v2+v3 > prev:
        desendCount+=1
    prev = v1+v2+v3

print( desendCount )