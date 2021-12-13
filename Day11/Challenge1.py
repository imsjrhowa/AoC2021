# AoC 2021 Day 11
# Challenge 22-23/50
# Answer  1735/400

import sys
import os
from collections import Counter

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []
field = []

def challenge1():
    ret = 0

    size = 5

    input = []
    flashField = []  
  
    with open(os.path.join(sys.path[0], "Simple.txt"), "r") as f:
        data = f.read()

    for line in data.splitlines():
        input.append( line )

    for l in range(len(input)):
        input[l] = (list(str(input[l])))

    for x in range(len(input[0])):
        for y in range(len(input[0])):
            input[x][y] = int(input[x][y])

    for index in range(size):
        flashField.append( [0] * size)

    def inc(field):
        for y in range(size):
            for x in range(size):
                input[y][x] = field[y][x] + 1

    def incAround(x:int, y:int):
        adj = [ 
                [-1,-1],[0,-1],[1,-1],
                [-1, 0],[1, 0],
                [-1, 1],[0, 1],[1, 1]
              ]

        for p in adj:
            if y+p[0]>=0 and y+p[0]<size and x+p[1]>=0 and x+p[1]<size:
                nx = x+p[1]
                ny = y+p[0]
                if flashField[ny][nx] != 1:
                    input[ny][nx] = input[ny][nx] + 1

    def eval():
        done = False
        flashCount = 0
        evalCount = 0
        while done == False:
            evalCount+=1
            print(evalCount)
            done = True
            for y in range(size):
                for x in range(size):
                    if input[y][x] > 9 and flashField[y][x] == 0:
                        done = False
                        input[y][x] = 0
                        flashField[y][x] = 1
                        flashCount += 1
                        incAround(x,y)
        return flashCount

    stepCount = 100

    #Challenge2
    #stepCount = 1000

    for step in range(stepCount):
        inc(input)
        r = eval()
        
        # Challenge 2
        #if r == 100:
        #    return step+1

        ret += r
        print("Step %d : %d" % (step+1, ret))
        flashField = []
        for index in range(size):
            flashField.append( [0] * size)

    return ret 


print("Answer 1 %d" % challenge1() )