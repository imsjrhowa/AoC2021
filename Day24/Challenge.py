# AoC 2021 Day 24
# Challenge 1

import sys
import os

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

A = read_input('Input.txt')
W = 0
X = 0
Y = 0
Z = 0
commands = []
MIN_Z = sys.maxsize

def ALU():
    global Z
    global X
    global Y
    global W
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


    def solve(place:int, value:str):
        global commands
        global W
        global X
        global Y
        global Z

        for command in commands[place]:
            if command[0] == 'i': # inp
                c, a = command.split(' ')
            else:
                c, a, b = command.split(' ')

            if c == 'inp':
                inp(a, str(value))
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

        return Z

    MEMO2 = {}
    def solveAll(place,input,z):
        place = 0
        global W
        global X
        global Y
        global Z
        W = X = Y = 0
        Z = z
        
        key = f'{place} {input} {z}'
        if key in MEMO2:
            return MEMO2[key]
        
        solve(place,str(input))
    
        MEMO2[key] = Z

        return Z
    
    MEMO = {}
    def find(place, z):
        global MIN_Z

        key = f'{place} {z}'
        if key in MEMO:
            return MEMO[key]

        found = None
        for input in (9,8,7,6,5,4,3,2,1):
            z_ret = solveAll(place,input,z)
            if place == 13:
                if abs(z_ret) < MIN_Z:
                    print(f'Min z {z_ret}')
                    MIN_Z = abs(z_ret)
                
                if z_ret == 0:
                    found = [input]
                    print("Found")
                    break
                else:
                    found = None
            else:
                new_found = find(place+1, z_ret)
                if new_found:
                    found = [input] + new_found
                    break
        
        MEMO[key] = found
        return found

# break up the commands into 14 lists..
    count = 0
    nlist = []
    for command in A:
        nlist.append(command)
        count += 1
        if count > 17:
            commands.append(nlist)
            nlist = []
            count = 0

    found = []
    found = find(0,0)

    # #startNum = 39924989499969
    # startNum  = 99999999999999
    # inputNumber = str(startNum)

    # W = X = Y = Z = 0
    # print( solve(0,inputNumber[0]) )
    # print( solve(1,inputNumber[1]) )
    # print( solve(2,inputNumber[2]) )
    # print( solve(3,inputNumber[3]) )
    # print( solve(4,inputNumber[4]) )
    # print( solve(5,inputNumber[5]) )
    # print( solve(6,inputNumber[6]) )
    # print( solve(7,inputNumber[7]) )
    # print( solve(8,inputNumber[8]) )
    # print( solve(9,inputNumber[9]) )
    # print( solve(10,inputNumber[10]) )
    # print( solve(11,inputNumber[11]) )
    # print( solve(12,inputNumber[12]) )
    # print( solve(13,inputNumber[13]) )
    # if Z == 0:
    #     print("Valid")

    return found

f = ALU()
print(f)
