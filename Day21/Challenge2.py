# AoC 2021 Day 21
# Challenge 2
# Answer 105619718613031

import itertools

p1 = 8
p2 = 2
UNIVERSE = {} 
def count_win(p1, p2, s1, s2):
  
    if s1 >= 21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
  
    if (p1, p2, s1, s2) in UNIVERSE:
        return UNIVERSE[(p1, p2, s1, s2)]
  
    ans = (0,0)
    for r in itertools.product(range(1, 4), repeat=3):
        new_p1 = (p1+sum(r))%10
        new_s1 = s1 + new_p1 + 1
        x1, y1 = count_win(p2, new_p1, s2, new_s1)
        ans = (ans[0]+y1, ans[1]+x1)

    UNIVERSE[(p1, p2, s1, s2)] = ans
    return ans



print("Challenge2 ", max(count_win(p1-1, p2-1, 0, 0)))