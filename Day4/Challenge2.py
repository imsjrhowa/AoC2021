# AoC 2021 Day 4
# Challenge 8/50
# Answer 19012

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
                    cards[card][line][index] = -999

    #printCards()

def printCards():
    i = 1
    for card in range(len(cards)):
        print("Card %d" % i)
        i+=1
        for line in range(len(cards[card])):
            print(cards[card][line])

def checkCards():
    #check left to right
    for card in range(len(cards)):
        for line in range(len(cards[card])):
            winner = True
            for index in range(5):
                if cards[card][line][index] != -999:
                    winner = False
            if winner == True:
                return card

    #check top to bottom
    for card in range(len(cards)):
        for index in range(5):
            winner = True
            for line in range(len(cards[card])):
                if cards[card][line][index] != -999:
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

wincount = 0
while len(callNumbers) > 0:
    number = drawNumber()
    print(number)
    applyNumberToCards(number)

    while checkCards() != -1: 
        winningCard = checkCards()
        if winningCard >= 0:
            wincount += 1
            print("Winning Card (%d)" % winningCard)
            print("Win Count %d" % wincount)
            ScoreValue = Score(winningCard)
            print("Answer %d" % (ScoreValue * number))
            del cards[winningCard] # remove winning card.

print("Done")
