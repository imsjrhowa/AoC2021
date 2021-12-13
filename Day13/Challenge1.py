# AoC 2021 Day 13
# Challenge 25-26/50
# Answer 847 / BCZRCEAB

import sys
import os
from collections import defaultdict, deque

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []
grid = []

maxX = 0
maxY = 0

bChallenge1 = False

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
    data = f.read()

E = []
F = []
for line in data.splitlines():

    # FOLD info
    if len(line) and line[0] == 'f':
        line = line.strip().split(' ')
        a,b = line[2].strip().split('=')
        F.append([a,b])  

    # POINTS info
    elif len(line):
        a,b = line.strip().split(',')

        # find width and hight of grid
        if int(a) > maxX:
            maxX = int(a)
        if int(b) > maxY:
            maxY = int(b)

        E.append([int(a),int(b)])  

maxX += 1
maxY += 1

for index in range(maxY):
    grid.append( [0] * maxX)

def finalGrid():
    for y in range(maxY):
        for x in range(maxX):
            c = ' '
            if grid[y][x] == 1:
                c = '#'
            sys.stdout.write("%c" % c)
        sys.stdout.write("\n\r")        

def foldAlongLine(foldDir:str, loc:str):
    global maxX
    global maxY

    foldLine = int(loc)
    if foldDir == 'y':       
        for y in range(maxY):
            for x in range(maxX):
                if foldLine+y >= maxY:
                    break

                if grid[foldLine+y][x] > 0:
                    grid[foldLine-y][x] = 1

        maxY = foldLine              

    else:
        for y in range(maxY):
            for x in range(maxX):
                if foldLine+x >= maxX:
                    break
                if grid[y][foldLine+x] > 0:
                    grid[y][foldLine-x] = 1                     
  
        maxX = foldLine

    return

def challenge1():
    ret = 0

    # Fill grid.
    for p in E:
        grid[p[1]][p[0]] = 1

    # Fold
    for f in F:
        foldAlongLine(f[0],f[1])        
        if bChallenge1:
            break
    
    # show grid for challenge 2
    if not bChallenge1:
        finalGrid()
        return 0

    # Score
    for y in range(maxY):
        for x in range(maxX):
            if grid[y][x] > 0:
                ret += 1
    return ret

print("Answer %d" % challenge1() )



