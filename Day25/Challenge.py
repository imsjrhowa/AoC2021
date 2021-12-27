# AoC 2021 Day 25
# Challenge 1
# Answer 412

import sys
import os

def read_input(fname, t=lambda x: x, strip_lines=True, force_multi=False):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        contents = f.read()
        return contents

A = read_input('Input.txt')
input = []

for line in A.splitlines():
    input.append( line )

for l in range(len(input)):
    input[l] = (list(str(input[l])))

sizeW = len(input[0])
sizeH = len(input)

def printGrid():
    for y in range(sizeH):
        for x in range(sizeW):
            sys.stdout.write("%c" % (input[y][x]))
        sys.stdout.write("\r\n")
    sys.stdout.write("\r\n")

def step():
    # move right
    moveW = {}
    for y in range( sizeH ):
        for x in range( sizeW ):
            c = input[y][x]
            key = f'{x} {y}'
            if c == '>':
                if x+1 < sizeW:
                    if input[y][x+1] == '.':
                        key = f'{x},{y},{x+1},{y}'
                        moveW[key] = 1
                elif x+1 == sizeW:
                    if input[y][0] == '.':
                        key = f'{x},{y},{0},{y}'
                        moveW[key] = 1

    for k in moveW.keys():
        x1,y1,x2,y2 = k.split(',')
        input[int(y2)][int(x2)] = input[int(y1)][int(x1)]
        input[int(y1)][int(x1)] = '.'

    # move down
    moveH = {}
    for x in range( sizeW ):
        for y in range( sizeH ):
            c = input[y][x]
            key = f'{x} {y}'
            if c == 'v':
                if y+1 < sizeH:
                    if input[y+1][x] == '.':
                        key = f'{x},{y},{x},{y+1}'
                        moveH[key] = 1
                elif y+1 == sizeH:
                    if input[0][x] == '.':
                        key = f'{x},{y},{x},{0}'
                        moveH[key] = 1

    for k in moveH.keys():
        x1,y1,x2,y2 = k.split(',')
        input[int(y2)][int(x2)] = input[int(y1)][int(x1)]
        input[int(y1)][int(x1)] = '.'

    return len(moveW) + len(moveH) 

def main():

    stepCount = 0
    while True:
        stepCount+=1
        if not step():
            print("Answer ", stepCount)
            break

    return 

main()