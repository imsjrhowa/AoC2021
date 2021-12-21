# AoC 2021 Day 20
# Challenge 1
# Answer 5622, 20395

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

D = read_input('Input.txt')
A = []
I = []
O = []

def binaryToDecimal(n):
    return int(n,2)

def challenge1():
    global I
    global A
    global O
    ret = 0
    
    A = D[0]
    Pad = 500
    for i in range(2,len(D)):
        I.append( '.'*Pad + D[i] + '.'*Pad )

    Lx = len(I[0])
    Ly = len(I)

    for _ in range(Pad):
        I.insert(0, '.' * Lx)
    for _ in range(Pad):
        I.insert(len(I), '.' * Lx)

    Lx = len(I[0])
    Ly = len(I)

    # small start
    # for i in range(2,len(D)):
    #     I.append( D[i] )

    # Lx = len(I[0])
    # Ly = len(I)
    # small end

    I = list(map(str.split, I))

    for loop in range(50):
        O = []
        for y in range(len(I)):
            out = []
            for x in range(len(I[0][0])):
                pixels = []
                for nx, ny in [ (x-1, y-1), (x,   y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1) ]:
                    if not len(I[0][0]) > nx >= 0 <= ny < len(I): # valid locaiton
                        pixels.append('0')
                        continue
                    if I[ny][0][nx] == '#':
                        pixels.append('1')
                    else:
                        pixels.append('0')

                pixels = "".join(pixels)
                index = binaryToDecimal(pixels)            
                out.append( A[index] )
            O.append(out) 
        nO = []
        for i in range(len(O)):           
            nO.append([''.join(O[i])])
        I = nO
        sys.stdout.write("Loop: %d        \r" % (loop))

    count = 0

    for y in range(100,len(I)-100):
        for x in range(100,len(I[0][0])-100):
            if I[y][0][x] == '#':
                count += 1

    ret = count
    return ret


print("Challenge1", challenge1())



