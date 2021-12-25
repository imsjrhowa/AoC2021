# AoC 2021 Day 24
# Challenge 1
# Answer 

import sys
import os
import numpy as np

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

A = read_input('SampleInput.txt')
W = 0
X = 0
Y = 0
Z = 0

def ALU():

    def inp(a,b):
        global X,W,Y,Z
        if a == 'w':
            W = int(b)
        elif a == 'x':
            X = int(b)
        elif a == 'y':
            Y = int(b)
        elif a == 'z':
            Z = int(b)
        else:
            print("ALU Error")

    def valueOf(a:str):
        global X,W,Y,Z
        if a == 'w':
            return W
        elif a == 'x':
            return X
        elif a == 'y':
            return Y
        elif a == 'z':
            return Z

    def add(a,b):
        global X,W,Y,Z
        if b.isnumeric() or b[0] == '-':
            num = valueOf(a) + int(b)
        else:
            num = valueOf(a) + valueOf(b)
        if a == 'w':
            W = num
        elif a == 'x':
            X = num
        elif a == 'y':
            Y = num
        elif a == 'z':
            Z = num
        else:
            print("ALU Error")

    def mul(a,b):
        global X,W,Y,Z
        num = 0
        if b.isnumeric() or b[0] == '-':
            num = valueOf(a) * int(b)
        else:
            num = valueOf(a) * valueOf(b)
        if a == 'w':
            W = num
        elif a == 'x':
            X = num
        elif a == 'y':
            Y = num
        elif a == 'z':
            Z = num
        else:
            print("ALU Error")

    def div(a,b):
        global X,W,Y,Z
        num = 0
        if b.isnumeric() or b[0] == '-':
            num = valueOf(a) // int(b)
        else:
            num = valueOf(a) // valueOf(b)

        if a == 'w':
            W = num
        elif a == 'x':
            X = num
        elif a == 'y':
            Y = num
        elif a == 'z':
            Z = num
        else:
            print("ALU Error")

    def mod(a,b):
        global X,W,Y,Z
        num = 0
        if b.isnumeric() or b[0] == '-':
            num = valueOf(a) % int(b)
        else:
            num = valueOf(a) % valueOf(b)

        if a == 'w':
            W = num
        elif a == 'x':
            X = num
        elif a == 'y':
            Y = num
        elif a == 'z':
            Z = num
        else:
            print("ALU Error")

    def eql(a,b):
        global X,W,Y,Z
        if b.isnumeric() or b[0] == '-':
            num = valueOf(a) == int(b)
        else:
            num = valueOf(a) == valueOf(b)

        num = int(num)            
        if a == 'w':
            W = num
        elif a == 'x':
            X = num
        elif a == 'y':
            Y = num
        elif a == 'z':
            Z = num
        else:
            print("ALU Error")

    found = []
    done = False
    startNum = 0
    i = 0
    while not done:
        startNum = startNum + 1
        inputNumber = str(startNum)

        if inputNumber == '9':
            return found


        while '0' in inputNumber:
            startNum = startNum + 1
            inputNumber = str(startNum)

        # if len(inputNumber) > 14:
        #     done = True
        #     return

      
        for command in A:

            if command[0] == 'i': # inp
                c, a = command.split(' ')
            else:
                c, a, b = command.split(' ')
    
            if c == 'inp':
                inp(a,inputNumber[i])
                #i+=1
            elif c == 'add':
                add(a,b)
            elif c == 'mul':
                mul(a,b)
            elif c == 'div':
                div(a,b)
            elif c == 'mod':
                mod(a,b)
            elif c == 'eql':
                eql(a,b)
            sys.stdout.write("%s                      \r" % (inputNumber))
            if Z == 0:            
                found.append(inputNumber)
    return found

f = ALU()
print(f)
