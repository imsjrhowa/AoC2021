# AoC 2021 Day 9
# Challenge 20/50
# Answer 448

import sys
import os

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []

def challenge1():
    ret = 0

    w = 100
    h = 100

    input = []    
    grid = []

    with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
        data = f.read()

    for line in data.splitlines():
        input.append( line.split() )
        grid.append( ["."] * w )

    def adj(x:int, y:int):
        c = int(input[y][0][x])
        l = r = u = d = 9
        #left
        if x - 1 >= 0:
            l = int(input[y][0][x-1])
        #right
        if x + 1 < w:
            r = int(input[y][0][x+1])
        #up
        if y - 1 >= 0:
            u = int(input[y-1][0][x])
        #down
        if y + 1 < h:
            d = int(input[y+1][0][x])

        if c < l and c < r and c < u and c < d:
            return True
        
        return False

    def apply(x:int, y:int):
        grid[y][x] = input[y][0][x]
        l = r = u = d = 9
        #left
        if x - 1 >= 0:
            grid[y][x-1] = "."
        #right
        if x + 1 < w:
            grid[y][x+1] = "."
        #up
        if y - 1 >= 0:
            grid[y-1][x] = "."
        #down
        if y + 1 < h:
            grid[y+1][x] = "."

    for y in range( h ):
        for x in range( w ):
            if adj(x,y):
                apply(x,y)

    
    for y in range(h):
        for x in range(w):
            if grid[y][x] != '.':
                ret += int(grid[y][x]) + 1

    return ret

print("Answer 1 %d" % challenge1() )
