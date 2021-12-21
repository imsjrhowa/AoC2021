# AoC 2021 Day 21
# Challenge 1
# Answer 513936

die = 0
dieRollCount = 0

def challenge1():

    def roll3():
        global die
        global dieRollCount
        count = 0
        ret = 0
        while count < 3:
            count += 1
            die += 1
            dieRollCount+=1
            if die > 100:
                die = 1
            ret += die

        return ret

    def move( playerPos:int, roll:int ):
        newPos = playerPos + roll
        while newPos > 10:
            newPos -= 10
        return newPos
    

    ret = 0
    p1_start = 8
    p2_start = 2

    p1_pos = p1_start
    p2_pos = p2_start
    p1_score = 0
    p2_score = 0

    turn = 0
    while p1_score != 1000 and p2_score != 1000:
        if turn == 0:
            p1_pos = move( p1_pos, roll3())
            p1_score += p1_pos
            turn = 1
            print("p1 ",p1_pos,p1_score)
        else:
            p2_pos = move( p2_pos, roll3())
            p2_score += p2_pos
            turn = 0
            print("p2 ",p2_pos,p2_score)

    if p1_score > p2_score:
        ret = p2_score * dieRollCount
    else:
        ret = p1_score * dieRollCount

    return ret

print("Challenge1 ", challenge1())
