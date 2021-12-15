# AoC 2021 Day 15
# Challenge 1
# Answer 487 

import sys
import os
import heapq

lines = []  

with open(os.path.join(sys.path[0], "SampleInput.txt"), "r") as f:
    data = f.read()

for line in data.splitlines():
    lines.append( line )

risks = [list(map(int, line)) for line in lines]
visited = [[0] * len(row) for row in risks]

paths = [(0, 0, 0)] # start

def challenge1():

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
    
print("Answer1 %d" % challenge1() )