# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:03:32 2021

@author: Krishna
"""

import random

a = random.randint(1,100)
print("random integers: ",a)

b = random.randrange(1,100)
print("numbers in range 1, 100 randomly: ",b)

c = random.randrange(1,100,2)
print("random odd numbers: ",c)

d = random.randrange(2,100,2)
print("random even numbers: ",d)

e = random.randrange(5,100,5)
print("random 5 multiples: ",e)

f = random.random()
# it return the numbers between 0 and 1
print("random numbers b/n 0 and 1: ",f)

a1 = random.choice([2,4,7,4,78,4,5,67])
print("random numbers from list: ",a1)



list = ['cat','dog','tiger','dragoon','zeus','pegasus','nemasis']
a2 = random.choice(list)
print("random words from list: ",a2)