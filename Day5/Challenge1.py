# AoC 2021 Day 5
# Challenge 9/50
# Answer 6666

import sys
import os

input = []
points = []
grid = []
maxX = 0
maxY = 0

def printGrid(width, hight):
    for x in range(width):
        for y in range(hight):
            sys.stdout.write(str(grid[x*width+y]))
        sys.stdout.write('\n')

def checkGridPoint(x,y):
    return grid[y*maxX+x]

def setGridPoint(x,y,value):
    grid[y*maxX+x] = value


with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
   lines = f.readlines()
   for line in lines:
       input.append(line.strip())

# Process input in to working data
for s in input:
    points.append( s.split(' -> ') )

for pair in range(len(points)):
    for set in range(2):
        points[pair][set] = points[pair][set].split(',')
        points[pair][set][0] = int(points[pair][set][0])
        points[pair][set][1] = int(points[pair][set][1])

# pair, start/end, x/y
#       0=start 1=end, x=0 y=1
# for pair in range(len(points)):
#     for point in range(2):
#         print( "%d [%d, %d]" % (pair, points[pair][point][0], points[pair][point][1]) )

# find max x and y
for pair in range(len(points)):
    for point in range(2):
        if points[pair][point][0] > maxX:
            maxX = points[pair][point][0]
        if points[pair][point][1] > maxY:
            maxY = points[pair][point][1]

maxX+=1
maxY+=1

# build grid
for x in range(maxX):    
    for y in range(maxY):
        grid.append(0)

for pair in range(len(points)):
    x1 = points[pair][0][0]
    y1 = points[pair][0][1]
    x2 = points[pair][1][0]
    y2 = points[pair][1][1]
    if x1 == x2:
        #print(pair)    
        if y1 < y2:
            for line in range((y2-y1)+1):
                v = checkGridPoint(x1,line+y1) + 1
                setGridPoint(x1,line+y1,v)
        else:
            for line in range((y1-y2)+1):
                v = checkGridPoint(x1,line+y2) + 1
                setGridPoint(x1,line+y2,v)        
        #printGrid(maxX, maxY)
    elif y1 == y2:
        #print(pair)    
        if x1 < x2:
            for line in range((x2-x1)+1):
                v = checkGridPoint(line+x1,y1) + 1
                setGridPoint(line+x1,y1,v)
        else:
            for line in range((x1-x2)+1):
                v = checkGridPoint(line+x2,y1) + 1
                setGridPoint(line+x2,y1,v)
        #printGrid(maxX, maxY)


#printGrid(maxX, maxY)
#print(points)

score = 0
for x in range(len(grid)):
    if grid[x] >= 2:
        score+=1

print(score)
