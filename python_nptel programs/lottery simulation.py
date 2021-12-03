# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:31:43 2021

LOTTERY SIMIULATION - PROfit OR LOSS

@author: Krishna
"""

import random
import sys
import matplotlib.pyplot as plt

account = 0
x = []
y = []

''' here x is an empty list for each day played
        y is an empty list for each day he won or loose or profit or loss
'''

for i in range(365):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    
    #print("players bet is: ",bet)
    #print("luck draw number is: ",luck_draw)
    
    if bet == lucky_draw:
        account = account + 900 - 100
        # Here 900 is the prize money
        # 100 is the cash paid to play the lottery
    else:
        account = account - 100
        # 100 is the cash paid to play the lottery
    
    y.append(account)
    #print("amount in your lottery game account is: ",account)

print("amount in your lottery game account is: ",account)

plt.plot(x,y)
plt.show()

print()
print("memory taken by list x variable: ",sys.getsizeof(x))