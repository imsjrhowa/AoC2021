# AoC 2021 Day 22
# Challenge 2
# Answer 1257350313518866

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

A = read_input('SampleInput.txt')

xs = []
ys = []
zs = []
action = []

for i in range(len(A)):
    A[i] = A[i].split(' ')
    if A[i][0] == 'on':
        A[i][0] = 1
    else:
        A[i][0] = 0

for i in range(len(A)):
    bOn = A[i][0]
    
    x,y,z = A[i][1].split(',')
    _, x = x.split('=')
    _, y = y.split('=')
    _, z = z.split('=')
    x1,x2 = x.split('..')
    y1,y2 = y.split('..')
    z1,z2 = z.split('..')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)

    A[i][1] = [[x1,x2],[y1,y2],[z1,z2]]

    # part 2
    action.append((bOn, (x1, x2), (y1, y2), (z1, z2)))
    xs.append(x1)
    xs.append(x2 + 1)
    ys.append(y1)
    ys.append(y2 + 1)
    zs.append(z1)
    zs.append(z2 + 1)

# this got me the right answer on the sample.. cross fingers.
action.reverse()

xs.sort() # smallest to largest.
ys.sort()
zs.sort()

count = 0

for x1,x2 in zip(xs, xs[1:]):
    print(f"x={x1}")
    # valid x's in actions
    ins_x = [(a, x, y, z) for a, x, y, z in action if x[0] <= x1 <= x[1]]

    for y1, y2 in zip(ys, ys[1:]):
        # valid y's in x's
        ins_y = [(a, x, y, z) for a, x, y, z in ins_x if y[0] <= y1 <= y[1]]

        for z1, z2 in zip(zs, zs[1:]):
            # test valid z in y's
            if next((a for a, x, y, z in ins_y if z[0] <= z1 <= z[1]), False):
                # if all poins are in the action then add all of them.
                count += (x2 - x1) * (y2 - y1) * (z2 - z1)


print(count)
