# AoC 2021 Day 19
# Challenge 1 - 2
# Answer 

import sys, os
from collections import *

def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def convertToInts(arr):
    out = []
    for v in arr:
        if is_int(v):
            out.append(int(v))
        else:
            out.append(v)
    return out

mps = [
    (0, 1),(1, 1),(2, 1),
    (0, -1),(1, -1),(2, -1)
]
directions = []
for p1 in mps:
    for p2 in mps:
        for p3 in mps:
            # if all 3 are diff...
            if len(set([p1[0], p2[0], p3[0]])) == 3:
                directions.append((p1, p2, p3))

def remap(d, coords):
    newCord = []
    for v in coords:
        newCord.append((
            d[0][1]*v[d[0][0]], d[1][1]*v[d[1][0]], d[2][1]*v[d[2][0]],
        ))
    return newCord

def deltaVar(p1, p2):
    return (p1[0] - p2[0], #x
            p1[1] - p2[1], #y
            p1[2] - p2[2]) #z

def find_match(s1, s2):
    for d in directions:
        newc = remap(d, s2)
        deltas = Counter()
        
        for p1 in s1:
            for p2 in newc:
                deltas[deltaVar(p1, p2)] += 1

        for k, v in deltas.items():
            if v < 12: continue
            newc2 = set()

            for p in newc:
                newc2.add((p[0]+k[0], 
                           p[1]+k[1], 
                           p[2]+k[2]))
                           
            return True, k, newc2
    return False, None, None

def solve(v):
    chunks = v.split('\n\n')
    scanners = []
    
    for chunk in chunks:
        lns = chunk.strip().split('\n')
        coords = []
        for l in lns[1:]:
            x, y, z = convertToInts(l.split(','))
            coords.append((x, y, z))
        scanners.append(coords)
    
    pts = set(scanners[0])
    pos = [(0, 0, 0)]

    q = list(enumerate(scanners))
    while q:
        q2 = []
        for i, sc in q:
            ok, scannerPos, extra = find_match(pts, sc)
            if ok:
                pts |= extra # add new points
                pos.append(scannerPos)
            else:
                q2.append((i, sc))
        q = q2

    # Challenge 2
    best = 0
    for p1 in pos:
        for p2 in pos:
            delta = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
            best = max(best, delta)

    return len(pts), best

def p1(v):
    count, _ = solve(v)
    return count

def p2(v):
    _, best = solve(v)
    return best

with open(os.path.join(sys.path[0], 'Input.txt'), "r") as f:
    A = f.read()

print(p2(A))