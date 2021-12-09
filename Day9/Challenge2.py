# AoC 2021 Day 9
# Challenge 21/50
# Answer 1417248

import sys
import os

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []

def challenge2():
    ret = 0

    w = 100
    h = 100

    input = []    
    grid = []
    basin = []
    basinSizes = []

    with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
        data = f.read()

    for line in data.splitlines():
        input.append( line.split() )
        grid.append( ["."] * w )
        basin.append( ["."] * w )

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

    def getAdj(x:int, y:int):
        c = int(input[y][0][x])
        basin[y][x] = str(c)       
     
        adjs = []
        l = r = u = d = 9
        #left
        if x - 1 >= 0:
            l = int(input[y][0][x-1])
            if l > c and l != 9:
                adjs.append( [x-1,y,l] )
        #right
        if x + 1 < w:
            r = int(input[y][0][x+1])
            if r > c and r != 9:
                adjs.append( [x+1,y,r] )
        #up
        if y - 1 >= 0:
            u = int(input[y-1][0][x])
            if u > c and u != 9:
                adjs.append( [x,y-1,u] )
        #down
        if y + 1 < h:
            d = int(input[y+1][0][x])
            if d > c and d != 9:
                adjs.append( [x,y+1,d] )

        # recurse
        for i in adjs:
            basin[i[1]][i[0]] = str(i[2])
            getAdj(i[0],i[1])     
        

    def spider(x:int, y:int):
        lows = []
        for y in range(h):
            for x in range(w):
                if grid[y][x] != '.':
                    lows.append( [x,y, int(grid[y][x])])
  
        for loc in lows:

            x = loc[0]
            y = loc[1]
            v = loc[2]
            getAdj( x,y )

            Score = 0
            for r in range(h):
                for c in range(w):
                    if basin[r][c] != '.':
                        Score+=1
                    basin[r][c] = '.'
            
            basinSizes.append(Score)

        basinSizes.sort(reverse=True)
        return basinSizes[0] * basinSizes[1] * basinSizes[2]

    # find lowest point apply to grid
    for y in range( h ):
        for x in range( w ):
            if adj(x,y):
                apply(x,y)

    #spider out lowiest point to find basin
    ret = spider(x,y)

    return ret

print("Answer 2 %d" % challenge2() )