# AoC 2021 Day 22
# Challenge 1
# Answer 653798

import sys
import os
import numpy as np

def read_input(fname, t=lambda x: x, strip_lines=True, force_multi=False):
    with open(os.path.join(sys.path[0], fname), "r") as f:
        contents = f.read()
    if strip_lines:
        lines = contents.strip().split('\n')
    else:
        lines = contents.split('\n')
    if len(lines) == 1 and not force_multi:
        return t(lines[0])
    return list(map(t, lines))

A = read_input('Input.txt')

for i in range(len(A)):
    A[i] = A[i].split(' ')
    if A[i][0] == 'on':
        A[i][0] = 1
    else:
        A[i][0] = 0

minS = sys.maxsize
maxS = 0

for i in range(len(A)):
    x,y,z = A[i][1].split(',')
    _, x = x.split('=')
    _, y = y.split('=')
    _, z = z.split('=')
    x1,x2 = x.split('..')
    y1,y2 = y.split('..')
    z1,z2 = z.split('..')

    x1 = int(x1)
    x2 = int(x2)

    y1 = int(y1)
    y2 = int(y2)

    z1 = int(z1)
    z2 = int(z2)

    if x1 >= -50 and x2 <= 50 and y1 >= -50 and y2 <= 50 and z1 >= -50 and z2 <= 50:
        if x1 < minS: minS = x1
        if y1 < minS: minS = y1
        if z1 < minS: minS = z1

        if x2 > maxS: maxS = x2
        if y2 > maxS: maxS = y2
        if z2 > maxS: maxS = z2
    else:
        A[i][0] = 2 # skip

    A[i][1] = [[x1,x2],[y1,y2],[z1,z2]]

maxS += 1
minS -= 1
gSize = maxS + abs(minS) 
G = np.zeros((gSize,gSize,gSize))

for i in range(len(A)):
    change = 0
    if A[i][0] != 2:
        if A[i][0] == 1: print("on")
        elif A[i][0] == 0: print("off")
        for x in range(A[i][1][0][0], A[i][1][0][1]+1):
            for y in range(A[i][1][1][0], A[i][1][1][1]+1):
                for z in range(A[i][1][2][0], A[i][1][2][1]+1):            
                    if G[x,y,z] != A[i][0]:
                        G[x,y,z] = A[i][0]
                        change += 1
    
        print(change)

count = 0
for x in range(len(G)):
    for y in range(len(G)):
        for z in range(len(G)):
            if G[x,y,z] == 1:
                count += 1

print(count)
