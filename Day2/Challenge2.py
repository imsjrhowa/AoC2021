# AoC 2021 Day 2
# Challenge 1
# Answer 1971232560

commands = []

with open(r'C:\Users\jerem\Documents\Projects\AoC2021\Day2\Input.txt') as f:
   lines = f.readlines()
   for line in lines:
       commands.append(line.strip())

commands = list(map(str.split, commands))

depth = 0
hPos = 0
aim = 0

for c in commands:
    command = c[0]
    change = int(c[1])

    if command == "forward":
        hPos += change
        if aim > 0:
            depth += aim * change    
    elif command == "up":
        aim -= change
    else:
        aim += change

print( depth * hPos )