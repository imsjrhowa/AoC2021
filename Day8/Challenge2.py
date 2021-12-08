# AoC 2021 Day 8
# Challenge 16/50
# Answer 

import sys
import os
import math
from statistics import mean

def SizeSort(lst):
    lst.sort(key=len)
    return lst

def search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return True
    return False

#signalSet = ['abcdeg', 'ab', 'acdfg', 'abcdf', 'abef', 'bcdef', 'bcdefg', 'abd', 'abcdefg', 'abcdef']
 
input = []
signals = []
digits = []

with open(os.path.join(sys.path[0], "Simple.txt"), "r") as f:
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

for i in range(len(signals)):
    for el in range(len(signals[i])):
        str1 = ""
        signals[i][el] = str1.join(signals[i][el])

for i in range(len(digits)):
    for el in range(len(digits[i])):
        #digits[i][el] = sorted(digits[i][el])
        str1 = ""
        digits[i][el] = str1.join(digits[i][el])

Answer = 0
for index in range( len(digits) ):
    found = []
    signalSet = []
    missing = []
    signalSet = signals[index]

    for i in range(len(signalSet)):
        str1 = ""
        signalSet[i] = str1.join(signalSet[i])
   
    signalSet = SizeSort(signalSet)
    #              1     2                     3        4                            5   solved
    #              |     |                     |        |                            | 
    #    000         bbb   bbb     bbb    bbb              bbb      bbb         bbb
    #    1 2     c     c   f         c      c      f c     f c      f           f c 
    #    333               ???     ???    ???      aaa     aaa      aaa         
    #    4 5     g     g     g     ?        g        g       g      ? g         ? g
    #    666               ???     ???    ???              ddd      ddd         ddd
    #           cg   gcb           
    #            1     7   5       2      3        4       9        6           0
    #                      -bdaec  bdaec  -bdaec   gfac    6-fgaebd  fgaebd     gdcbef
    #                      gdafb  -bgcad  bgcad            agbcfd
    #                      -bgcad                          0-gdcbef 
    # 
    #                              
    # ['cg', 'gcb', 'gfac', 'bdaec', 'gdafb', 'bgcad', 'fgaebd', 'agbcfd', 'gdcbef', 'cdgabef']

    sevenSeg = [' ',' ',' ',' ',' ',' ',' ']
    print(signalSet)
    for i in range(len(signalSet)):
        signalSize = len(signalSet[i])
        if signalSize == 2:
            print(signalSet[i])
            sevenSeg[2] = signalSet[i][0]
            sevenSeg[5] = signalSet[i][1]
        elif signalSize == 3:
            print(signalSet[i])
            for c in range(len(signalSet[i])):
                if search(sevenSeg, signalSet[i][c]) == False:
                    sevenSeg[0] = signalSet[i][c]                    
        elif signalSize == 4:
            print(signalSet[i])
            sevenSeg[1] = signalSet[i][1]
        elif signalSize == 7:            
            print("8")
        # else:

    for v in range(4):
        signalSize = len(digits[index][v])
        if signalSize == 2:
            found.append(1)
        elif signalSize == 3:
            found.append(7)
        elif signalSize == 4:
            found.append(4)
        elif signalSize == 7:
            found.append(8)
        else:
            bFound = False
            for d in range(len(signalSet)):
                if digits[index][v] == signalSet[d]:
                    bFound = True
                    found.append(d)
            if bFound == False:                        
                missing.append(digits[index][v])
                found.append(0)

    if found[0] < 0 or found[1] < 0 or found[2] < 0 or found[3] < 0:
        print("error")
    else:
        Answer += 1000*found[0] + 100*found[1] + 10*found[2] + 1*found[3]

missing = list(set(missing))
print(missing)

print("Answer %d" % Answer)
