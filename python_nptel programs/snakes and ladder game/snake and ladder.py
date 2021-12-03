# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:02:50 2021

SNAKE AND LADDER GAME

@author: Krishna
"""

from PIL import Image
import random

end = 100
print(" WELCOME TO THE SNAKE AND LADDERS GAME ")
print()

def show_board():
    img = Image.open('snake.jpg')
    img.show()

def check_ladder(points):
    if points == 8:
        print("you are in ladder")
        return 26
    elif points == 21:
        print("you are in ladder")
        return 82
    elif points == 43:
        print("you are in ladder")
        return 77
    elif points == 50:
        print("you are in ladder")
        return 91
    elif points == 54:
        print("you are in ladder")
        return 93
    elif points == 62:
        print("you are in ladder")
        return 96
    elif points == 66:
        print("you are in ladder")
        return 87
    elif points == 80:
        print("you are in ladder")
        return 100
    else:
        print(" you not in a ladder ")
        return points

def check_snake(points):
    if points == 44:
        print(" you are bitten by a snake ")
        return 22
    elif points == 46:
        print(" you are bitten by a snake ")
        return 5
    elif points == 48:
        print(" you are bitten by a snake ")
        return 9
    elif points == 52:
        print(" you are bitten by a snake ")
        return 11
    elif points == 55:
        print(" you are bitten by a snake ")
        return 7
    elif points == 59:
        print(" you are bitten by a snake ")
        return 17
    elif points == 64:
        print(" you are bitten by a snake ")
        return 36
    elif points == 69:
        print(" you are bitten by a snake ")
        return 33
    elif points == 73:
        print(" you are bitten by a snake ")
        return 1
    elif points == 83:
        print(" you are bitten by a snake ")
        return 19
    elif points == 92:
        print(" you are bitten by a snake ")
        return 51
    elif points == 95:
        print(" you are bitten by a snake ")
        return 24
    elif points == 98:
        print(" you are bitten by a snake ")
        return 28
    else:
        print(" you are not bitten by a snake ")
        return points
    
def reached_end(points):
    if points == end:
        return 1
    else:
        return 0
    
def play():
    
    p1_name = input("player 1 please enter your name: ")
    p2_name = input("player 2 please enter your name: ")
    # here p1_name and p2_name are player names
    
    pp1 = 0
    pp2 = 0
    # where pp1 and pp2 are player 1 and player 2 points initially
    
    turn = 0
    while 1:
        if turn%2 == 0:
            # player 1 turn
            print(p1_name," it's your turn ")
            
            c = int(input("press 1 to continue or press 0 to quit the game: "))
            if c == 0:
                print(p1_name," score: ",pp1)
                print(p2_name," score: ",pp2)
                print(" quitting the game, thanks for playing ")
                break
            
            dice = random.randint(1,6)
            print(" dice rolled is: ",dice)
            pp1 = pp1 + dice
            
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            
            # check if the player goes beyond the board
            if pp1 > end:
                pp1 = end
            
            print(p1_name," your score is: ",pp1)
            
            if reached_end(pp1):
                print(p1_name," you won the game ")
                break
        else:
            print()
            # player 2 turn
            print(p2_name," it's your turn ")
            
            c = int(input("press 1 to continue or press 0 to quit the game: "))
            if c == 0:
                print(p1_name," score: ",pp1)
                print(p2_name," score: ",pp2)
                print(" quitting the game, thanks for playing ")
                break
            
            dice = random.randint(1,6)
            print(" dice rolled is: ",dice)
            pp2 = pp2 + dice
            
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            
            # check if the player goes beyond the board
            if pp2 > end:
                pp2 = end
            
            print(p2_name," your score is: ",pp2)
            
            if reached_end(pp2):
                print(p2_name," you won the game ")
                break
            
        turn = turn + 1
   
show_board()
play()