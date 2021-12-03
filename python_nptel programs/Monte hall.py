# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 17:32:00 2021

MONTE HALL MINI GAME CODE

@author: Krishna
"""

import random

doors = [0]*3
goatdoor = [0]*3
swap = 0 # no. of swap wins
dont_swap = 0 # no.of dont_swap wins
j = 0

n = int(input('how many times yu want to play: '))
while j < n:
    x = random.randint(0,2)
    doors[x] = 'BMW'
    for i in range(0,3):
        if i == x:
            continue
        else:
            doors[i] = 'goat'
            goatdoor.append(i)
    
    choice = int(input("enter your choice in b/n 0 to 2: "))
    door_open = random.choice(goatdoor)
    
    while door_open == choice:
        door_open = random.choice(goatdoor)
    
    ch = input("Do you want to swap? yes/no  ")
    if ch == 'yes':
        if doors[choice] == 'goat':
            print(" PLAYER  WINS ")
            swap += 1
        else:
            print(" PLAYER LOST ")
    else:
        if doors[choice] == 'goat':
            print(" PLAYER LOST ")
        else:
            print(" PLAYER WINS ")
            dont_swap += 1
            
    j += 1
    
    
print("no.of swap wins: ",swap)
print("no.of don't swap wins: ",dont_swap)