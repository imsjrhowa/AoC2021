# AoC 2021 Day 17
# Challenge 1
# Answer 6441

import sys

def challenge1():
    #target area: x=153..199, y=-114..-75
    x1, x2 = 153, 199
    y1, y2 = -114, -75

    ans = 0
    for x in range(500):
        for y in range(500):
            xv, yv = x, y
            curX = curY = 0
            pos = False
            maxY = 0
            for times in range(500):
                curX += xv
                curY += yv
                maxY = max(maxY, curY)
                if xv > 0: xv -= 1
                if xv < 0: xv += 1
                yv -= 1
                if y1 <= curY <= y2 and x1 <= curX <= x2:
                    pos = True
                    break
            if pos:
                ans = max(ans, maxY)            
            sys.stdout.write("x: %d y: %d            \r" % (x,y))
    sys.stdout.write("\n\r")
    return ans

print("Answer1 %d" % challenge1())



