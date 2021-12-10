# AoC 2021 Day 10
# Challenge 22/50
# Answer 4038824534

import sys
import os
import math
from collections import Counter

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []

def challenge2():
    ret = 0

    input = []    

    with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
        data = f.read()

    for line in data.splitlines():
        input.append( line )

    for l in range(len(input)):
        input[l] = list(str(input[l]))

    def isOpen(c:str):
        if c == '(' or c == '[' or c == '{' or c == '<':
            return True        
        return False

    def getPair(c:str):
        if c == '(':
            return ')'
        elif c == '[':
            return ']'
        elif c == '{':
            return '}'
        elif c == '<':
            return '>'
        return ' '

    def score(c:str):
        if c == ')':
            return 1
        elif c == ']':
            return 2
        elif c == '}':
            return 3
        elif c == '>':
            return 4

    def crawl(string:str):
        find = []
        ret = 0
        for i in range(len(string)):
            if isOpen(string[i]):
               find.append(string[i])
               string[i] = ' '
            else:
                f = find[-1]
                c = string[i]
                if c == getPair(f):
                    del find[-1]
                    string[i] = ' '
                else:
                    return 0

        if len(find) > 0:
            find.reverse()
            for i in range(len(find)):
                find[i] = getPair(find[i])                
                ret = (ret * 5) + score(find[i])

        return ret

    Scores = []
    for l in input:
        r = crawl(l)
        if r > 0:
            Scores.append(r)

    Scores = sorted(Scores)
    ret = Scores[ math.floor(len(Scores)/2) ]
    return ret
  

print("Answer 1 %d" % challenge2() )