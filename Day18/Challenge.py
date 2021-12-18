# AoC 2021 Day 18
# Challenge 1
# Answer 


from bisect import *
from collections import *
from functools import *
from heapq import *
import itertools
from string import whitespace, ascii_lowercase, ascii_uppercase, ascii_letters, digits, hexdigits, octdigits, punctuation, printable

import sys
import os

lines = [] 
input = []
data =[]

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

A = read_input("SampleInput.txt")

def challenge1():
    ret = 0    

    # [1,2]
    # [[1,2],3]
    # [9,[8,7]]
    # [[1,9],[8,5]]
    # [[[[1,2],[3,4]],[[5,6],[7,8]]],9]

    N = len(A)
    acc = eval(A[0])

    for i in range(1, N):
        b = eval(A[i])
        acc = [acc, b]


    #s = [ '[','[','[','[','[','9',',','8',']',',','1',']',',','2',']',',','3',']',',','4',']' ]
    s = [ '[','9',',','8',']' ]


     # HERE
    return ret

print("Answer1 %d" %challenge1())