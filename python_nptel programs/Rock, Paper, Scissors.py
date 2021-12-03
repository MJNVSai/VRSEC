# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:26:31 2021

ROCK PAPER SCISSOR GAME MINI CODE WITH OUT CHEATING

@author: Krishna
"""

def rps(num1,num2,bit1,bit2):
    p1 = int(num1[bit1])%3
    p2 = int(num2[bit2])%3
    # p1,p2 are player1 and player2
    
    if player_one[p1] == player_two[p2]:
        print(" game is draw ")
    elif player_one[p1] == 'rock' and player_two[p2] == 'scissor':
        print(" Player 1 wins ")
    elif player_one[p1] == 'rock' and player_two[p2] == 'paper':
        print(" Player 2 wins ")
    elif player_one[p1] == 'paper' and player_two[p2] == 'scissor':
        print(" Player 2 wins ")
    elif player_one[p1] == 'paper' and player_two[p2] == 'rock':
        print(" Player 1 wins ")
    elif player_one[p1] == 'scissor' and player_two[p2] == 'rock':
        print(" Player 2 wins ")
    elif player_one[p1] == 'scissor' and player_two[p2] == 'paper':
        print(" Player 1 wins ")
        
        
player_one = {0:'rock',1:'paper',2:'scissor'}
player_two = {0:'paper',1:'rock',2:'scissor'}

while 1:
    num1 = input("player 1 enter your number: ")
    num2 = input("player 2 enter your number: ")
    bit1 = int(input("player 1 enter your secret bit position: "))
    bit2 = int(input("player 2 enter your secret bit position: "))
    
    rps(num1, num2, bit1, bit2)
    
    ch = input("do you want to continue? yes/no  ")
    if ch == 'no':
        break
    
    
