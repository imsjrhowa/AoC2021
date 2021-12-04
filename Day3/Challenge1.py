# AoC 2021 Day 3
# Challenge 5/50
# Answer 3885894
import sys
import os

def binaryToDecimal(n):
    return int(n,2)

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1 

def invertBits(s):
    str1 = ""
    for ele in s:
        if ele == '1':
            str1 += '0'
        else:
            str1 += '1'
    return str1

values = []

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
   lines = f.readlines()
   for line in lines:
       values.append(line.strip())


values = list(map(str.split, values))

bitValues = []

bitCount = 12
for i in range(bitCount):
    bitValues.append(0)

for str in values:
    for b in range(bitCount):
        if str[0][b] == "1":
            bitValues[b] += 1

count = len(values)

bits = []

for b in range(bitCount):
    if (count - bitValues[b]) < bitValues[b]:
        bits.append("1")
    else:
        bits.append("0")

gammaRate = int(binaryToDecimal(listToString(bits)))
epsilon = int(binaryToDecimal(listToString(invertBits(bits))))

print (gammaRate * epsilon)

