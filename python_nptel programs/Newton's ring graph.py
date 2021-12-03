# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 10:03:55 2021

@author: Krishna
"""

# to draw the graph of the newtons rings
import matplotlib.pyplot as plt

a = [1,2,3,4,5,6,7,8,9,10]
# a is an no.of rings

b = [0.0098,0.046,0.067,0.0924,0.1239,0.1317,0.156,0.1849,0.2079,0.25]
# b is an square of the diameter

plt.plot(a,b,'bs')
plt.plot(a,b)

plt.xlabel('no.of rings')
plt.ylabel('square of an diameter')