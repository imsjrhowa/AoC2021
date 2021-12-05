# AoC 2021 Day 4
# Challenge 7/50
# Answer 21607

import sys
import os

input = []
callNumbers = []
cards = []

def drawNumber():
    if len(callNumbers) <= 0:
        return -1

    num = callNumbers[0]
    del callNumbers[0]
    return int(num)
 
def applyNumberToCards( num ):
    for card in range(len(cards)):
        for line in range(len(cards[card])):
            for index in range(5):
                if cards[card][line][index] == num:
                    cards[card][line][index] = -num

def checkCards():
    #check left to right
    for card in range(len(cards)):
        for line in range(len(cards[card])):
            winner = True
            for index in range(5):
                if cards[card][line][index] >= 0:
                    winner = False
            if winner == True:
                return card

    #check top to bottom
    for card in range(len(cards)):
        for index in range(5):
            winner = True
            for line in range(len(cards[card])):
                if cards[card][line][index] >= 0:
                    winner = False
            if winner == True:
                return card

    return -1

def Score(card):
    sum = 0
    for line in range(len(cards[card])):
        for index in range(5):
            if cards[card][line][index] >= 0:
                sum += cards[card][line][index]
    
    return sum


with open(os.path.join(sys.path[0], "Input.txt"), "r") as f:
   lines = f.readlines()
   for line in lines:
       input.append(line.strip())

# parse data file.
callNumbers = input[0].split(',')

fptr = 1

while( fptr < len(input) ):
    fptr+=1 #space
    nCard = []
    nCard.append( list(map(int, input[fptr].split())) ) 
    fptr+=1
    nCard.append( list(map(int, input[fptr].split())) ) 
    fptr+=1
    nCard.append( list(map(int, input[fptr].split())) ) 
    fptr+=1
    nCard.append( list(map(int, input[fptr].split())) ) 
    fptr+=1
    nCard.append( list(map(int, input[fptr].split())) ) 
    fptr+=1
    cards.append(nCard)

winner = False
while winner == False:
    #Draw Number
    number = drawNumber()
    applyNumberToCards(number)
    winningCard = checkCards()
    if winningCard >= 0:
        print("Winning Card (%d)" % winningCard)
        ScoreValue = Score(winningCard)

        print(ScoreValue)
        print(number)
        print("Answer %d" % (ScoreValue * number))
        winner = True
