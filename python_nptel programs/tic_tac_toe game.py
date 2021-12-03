# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:36:09 2021

TIC TAC TOE GAME CODE

@author: Krishna
"""

import numpy as np

board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])

p1s = 'X'
p2s = 'O'

''' p1s and p2s are the player1 symbol , player2 symbol '''

def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(np.matrix(board))
            print(symbol,' WON ')
            return True
    return False

def check_cols(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[c][r] == symbol:
                count += 1
        if count == 3:
            print(np.matrix(board))
            print(symbol,' WON ')
            return True
    return False

def check_diagonals(symbol):
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == symbol:
        print(np.matrix(board))
        print(symbol,' WON ')
        return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == symbol:
        print(np.matrix(board))
        print(symbol,' WON ')
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(np.matrix(board))
    
    while 1:
        row = int(input("enter row ==> 1 or 2 or 3: "))
        col = int(input("enter column ==> 1 or 2 or 3: "))
        
        if row > 0 and row < 4 and col > 0 and col < 4 and board[row-1][col-1] == '-':
            break
        else:
            print("INVALID INPUT. PLEASE ENTER AGAIN")
    
    board[row-1][col-1] = symbol
    
def play():
    for turn in range(9):
        if turn%2 == 0:
            print(" it's  X TURN's ")
            place(p1s)
            
            if won(p1s):
                break
        else:
            print(" it's O TURN's ")
            place(p2s)
            
            if won(p2s):
                break
    
    if not(won(p1s)) and not(won(p2s)):
        print(" THE GAME IS DRAW ")
        
play()

print(__doc__) 