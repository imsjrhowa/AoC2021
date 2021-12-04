# AoC 2021 Day 3
# Challenge 6/50
# Answer 

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

def keep(bitArray, checkBit, value):
    nArray = []

    for b in bitArray:
        if b[0][checkBit] == value:
            nArray.append(b[0])

    nArray = list(map(str.split, nArray))
    return nArray

bitCount = 12
values = []

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
   lines = f.readlines()
   for line in lines:
       values.append(line.strip())

values = list(map(str.split, values))
keepValues = []
keepValues = values
bitToCheck = 0
while len(keepValues) > 1 and bitToCheck < bitCount :
    v0 = keep( keepValues, bitToCheck, "0")
    v1 = keep( keepValues, bitToCheck, "1")

    if len(v0) > len(v1):
        keepValues = v0
    else:
        keepValues = v1

    print(keepValues)
    bitToCheck+=1

oxygenGenRating = binaryToDecimal( listToString(keepValues[0]) )
print( oxygenGenRating )

keepValues = []
keepValues = values
bitToCheck = 0
while len(keepValues) > 1 and bitToCheck < bitCount :
    v0 = keep( keepValues, bitToCheck, "0")
    v1 = keep( keepValues, bitToCheck, "1")

    if len(v0) <= len(v1):
        keepValues = v0
    else:
        keepValues = v1

    print(keepValues)
    bitToCheck+=1

oxygeCO2ScrubberRating = binaryToDecimal( listToString(keepValues[0]) )

print( oxygeCO2ScrubberRating )

print ("Answer: %d" % (oxygenGenRating * oxygeCO2ScrubberRating) )
