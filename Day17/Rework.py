 #target area: x=153..199, y=-114..-75
x1, x2, y1, y2 = 153, 199, -114, -75

x, y = 0, 0


def update(x, y, xv, yv):
    x += xv
    y += yv

    if xv > 0:
       xv -= 1
    elif xv < 0:
       xv += 1
    else:
       xv = 0
    yv -= 1
    return x, y, xv, yv


hit_cnt = 0
max_ys = []
for ix in range(1, x2+1): #1 - 200 
    for iy in range(y1, abs(y1)): #-144 - 75
        xv, yv = ix, iy
        x, y = 0, 0

        ys = []
        while True:
            x,y,xv,yv = update(x,y,xv,yv)
            ys.append(y)
            if x in list(range(x1,x2+1)) and y in list(range(y1,y2+1)):
                max_ys.append(max(ys))
                break
            elif x > x2 or y < y1: # early out.. speed.
                break 

print(max(max_ys))
print(len(max_ys))