# AoC 2021 Day 6
# Challenge 12/50
# Answer 1675781200288

import sys
import os

input =[]
school = []

newschool = []

def getSum(num):
    count = 0
    for i in school:
        if i == num:
            count += 1
    return count

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
   lines = f.readlines()
   for line in lines:
       input.append(line.strip())

input = input[0].split(',')
school = list(map(int, input))
#             0,1,2,3,4,5,6,7,8
poolSchool = [0,0,0,0,0,0,0,0,0]

for fish in range(len(school)):
    poolSchool[school[fish]] += 1

print(school)
print(poolSchool)

day = 1
challenge1 = False

while day <= 256:

    if challenge1:
        for fish in range(len(school)):
            school[fish] -= 1
            if school[fish] == -1:
                school[fish] = 6 #fish reset
                school.append(8) #new fish

        sys.stdout.write("Day %d : %d\r\n" % (day,len(school)))

    else: #challenge 2
        f0 = poolSchool[0]
        f1 = poolSchool[1]
        f2 = poolSchool[2]
        f3 = poolSchool[3]
        f4 = poolSchool[4]
        f5 = poolSchool[5]
        f6 = poolSchool[6]
        f7 = poolSchool[7]
        f8 = poolSchool[8]
        
                     # 0, 1, 2, 3, 4, 5,    6, 7, 8
        poolSchool = [f1,f2,f3,f4,f5,f6,f7+f0,f8,f0]

        count = sum(poolSchool)

        sys.stdout.write("Day %d : [ %d,%d,%d,%d,%d,%d,%d,%d,%d] : %d\r\n" % (day,f0,f1,f2,f3,f4,f5,f6,f7,f8,count))

    day+=1

sys.stdout.write("\r\n")
