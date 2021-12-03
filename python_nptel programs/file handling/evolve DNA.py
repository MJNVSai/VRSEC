# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:41:41 2021

@author: Krishna
"""

import random
def evolve(x):
    ind = random.randint(0,len(x)-1)
    p = random.randint(1,100)
    if p == 1:
        if x[ind] == '0':
            x[ind] = '1'
        else:
            x[ind] = '0'


with open("DNA.txt") as myfile:
    x = myfile.read()
    x = list(x)
for i in range(0,10000):
    evolve(x)
    
    
print(x)