# AoC 2021 Day 8
# Challenge 18/50
# Answer 1004688

import sys
import os

# Found a new way to load a file from the local directory
local_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(local_dir, ".."))

data = []

def challenge2():
    ret = 0

    # Just read all the data here..
    with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
        data = f.read()

    for line in data.splitlines():
        wires_list_s, output = line.split(" | ")
        wires_list = ["".join(sorted(wires)) for wires in wires_list_s.split()]
        wires_map = [""] * 10

        # find known numbers using the number of wires
        len_num_map = {2: 1, 3: 7, 4: 4, 7: 8}
        for wires in wires_list:
            if len(wires) in len_num_map:
                wires_map[len_num_map[len(wires)]] = wires

        # find all unknown numbers by checking which wires are in common with known
        # wires as well as using its number of wires
        for wires in wires_list:
            if wires in wires_map:
                continue

            c = set(wires)
            if len(c & set(wires_map[1])) == 1:
                # 2, 5, or 6
                if len(c & set(wires_map[4])) == 2:
                    wires_map[2] = wires
                else:
                    # 5 or 6
                    if len(c) == 5:
                        wires_map[5] = wires
                    else:
                        assert len(c) == 6
                        wires_map[6] = wires
            else:
                # 0, 3, or 9
                if len(c) == 5:
                    wires_map[3] = wires
                else:
                    if len(c & set(wires_map[4])) == 4:
                        wires_map[9] = wires
                    else:
                        wires_map[0] = wires

        num = ""
        for wires in output.split():
            wires = "".join(sorted(wires))
            num += str(wires_map.index(wires))
   
        ret += int(num)
    return ret

print( "Answer %d" % challenge2() )
