# AoC 2021 Day 12
# Challenge 24-25/50
# Answer  4912 / 150004

import sys
import os
from collections import defaultdict, deque

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []

with open(os.path.join(sys.path[0], "SampleInput.txt"), "r") as f:
    data = f.read()

E = defaultdict(list) # default_factory using list.
for line in data.splitlines():
    a,b = line.strip().split('-')
    E[a].append(b)
    E[b].append(a)

def challenge1():
    ret = 0

    # start, smallCave?
    start = ('start', set(['start']))

    Q = deque([start])

    while Q:            
        pos, small = Q.popleft()

        if pos == 'end':
            ret += 1
            continue
            
        # E at pos[start] = [A,b]
        for y in E[pos]:  # E at pos that is the key to the dict       
            # small cave only once.          
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y) # add small
                Q.append((y, new_small))

    return ret

def challenge2():
    ret = 0

    #Challenge2 adds small caves can be seen twice
    start = ('start', set(['start']), None)

    Q = deque([start])

    while Q:            
        pos, small, twice = Q.popleft()
        if pos == 'end':
             ret += 1
             continue
        for y in E[pos]:            
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small, twice))
 
            # have we seen this small cave twice?
            elif y in small and twice is None and y not in ['start', 'end']:
                Q.append((y, small, y))

    return ret

print("Answer 1 %d" % challenge1() )
print("Answer 2 %d" % challenge2() )