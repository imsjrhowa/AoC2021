# AoC 2021 Day 14
# Challenge 27/50
# Answer 2602

import sys
import os
from collections import defaultdict

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []
lines = []
sSeq = ""
with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
    data = f.read()

first = True
E = defaultdict(list)
V = defaultdict(list)
for line in data.splitlines():
    if len(line) > 0:
        if first:
            sSeq = line
            first = False
        else:
            p, r = line.split(' -> ')
            E[p].append(r)

def step():
    nSeq = []
    nSeq += sSeq[0]
    for i in range(len(sSeq)):
        if len(sSeq) <= i+1:
            return nSeq
        key = sSeq[i] + sSeq[i+1]
        nSeq += E[key]
        nSeq += sSeq[i+1]
    return nSeq


def challenge1():
    global sSeq

    for i in range(10):
        sSeq = step()
        sys.stdout.write("step: %d            \r" % i+1)
    sys.stdout.write("\n\r")

    for i in range(len(sSeq)):
        key = sSeq[i]
        if key not in V:
            V[key].append(0)
        V[key][0] += 1

    sorted_values = sorted(V.values(), reverse=True) # Sort the values
    sorted_dict = {}

    for i in sorted_values:
        for k in V.keys():
            if V[k] == i:
                sorted_dict[k] = V[k]
                break

    large = sorted_dict[list(sorted_dict.keys())[0]]
    small = sorted_dict[list(sorted_dict.keys())[-1]]
    ret = large[0] - small[0] 
    return ret

print("Answer %d" % challenge1())