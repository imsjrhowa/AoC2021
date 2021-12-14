# AoC 2021 Day 14
# Challenge 28/50
# Answer 2942885922173

import sys
import os
from collections import defaultdict
from collections import Counter

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []
lines = []
sSeq = ""

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
    data = f.read()

first = True
E = defaultdict(list)
for line in data.splitlines():
    if len(line) > 0:
        if first:
            sSeq = line
            first = False
        else:
            p, r = line.split(' -> ')
            E[p].append(r)

def step(cnt):
    ncnt = Counter()
    for k, v in cnt.items():
        if k in E:
            c = E[k]
            ncnt[k[0] + c[0]] += v
            ncnt[c[0] + k[1]] += v
        else:
            ncnt[k] += v # bad?
    return ncnt


def challenge1():
    global sSeq
    cnt = Counter(sSeq[i:i+2] for i in range(len(sSeq)-1))
    for i in range(40):
        cnt = step(cnt)

    lcnt = Counter()
    for k, v in cnt.items():
        lcnt[k[1]] += v

    lcnt[sSeq[0]] += 1
    ret = max(lcnt.values()) - min(lcnt.values())
    return ret

print("Answer %d" % challenge1())