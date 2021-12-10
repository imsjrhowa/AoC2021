# AoC 2021 Day 10
# Challenge 21/50
# Answer 268845

import sys
import os
from collections import Counter

local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []

def challenge1():
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

    def isClose(c:str):
        if c == ')' or c == ']' or c == '}' or c == '>':
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

    def crawl(string:str):
        find = []

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
                    return c # corrupted

        for i in range(len(string)):
            if string[i] != ' ':
                return 'i' # Incomplete

        return 'v' # Valid

    corrupted = []
    for l in input:
        r = crawl(l)
        if r == 'i':
            print("Incomplete")
        elif r == 'v':
            print("Valid")
        else:
            corrupted.append(r)

    corrupted = sorted(corrupted)
    out = Counter(corrupted)
    ret = out[")"] * 3 + out["]"] * 57 + out["}"] * 1197 + out[">"] * 25137

    return ret
  

print("Answer 1 %d" % challenge1() )