# AoC 2021 Day 6
# Challenge 11/50
# Answer 372300

import sys
import os

input =[]
school = []

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
   lines = f.readlines()
   for line in lines:
       input.append(line.strip())

input = input[0].split(',')
school = list(map(int, input))

day = 1
while day <= 256:
    for fish in range(len(school)):
        school[fish] -= 1
        if school[fish] <= -1:
            school[fish] = 6 #fish reset
            school.append(8) #new fish

    sys.stdout.write("Day %d : %d\r" % (day,len(school)))
    day+=1

sys.stdout.write("\r\n")