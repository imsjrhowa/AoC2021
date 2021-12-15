# AoC 2021 Day 15
# Challenge 2
# Answer 2821 

import sys
import os
import heapq

lines = []  

with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
    data = f.read()

for line in data.splitlines():
    lines.append( line )

_risk = [list(map(int, line)) for line in lines]

def wrap(x):
    return(x - 1) % 9 + 1

risks = [[0] * len(row) * 5 for row in _risk * 5]

r = len(_risk)
c = len(_risk[0])

for i in range(len(risks)):
    for j in range(len(risks[i])):
        risks[i][j] = wrap(_risk[i % r][j % c] + i // r + j // c)

visited = [[0] * len(row) for row in risks]

paths = [(0, 0, 0)] # start
def challenge2():

    while True:
        risk, x, y = heapq.heappop(paths)
        if visited[x][y] >= 1: 
            continue

        # found end?
        if (x, y) == (len(risks) - 1, len(risks[x]) - 1):
            return risk

        visited[x][y] = 1
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if not len(risks) > nx >= 0 <= ny < len(risks[0]): 
                continue
            if visited[nx][ny]: 
                continue

            # risk goes first so that its sorted in the heap.
            heapq.heappush(paths, (risk + risks[nx][ny],nx,ny))
    
print("Answer2 %d" % challenge2() )