# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 13:41:50 2021

@author: Krishna
"""

# to draw the field along the axis of the coil of a graph
import matplotlib.pyplot as plt

x = [0,5,10,15,20]
y = [0.452,0.318,0.181,0.0842,0.033]

x1 = [-5,-10,-15,-20]
y1 = [-0.302,-0.159,-0.0466,-0.0315]

plt.plot(x,y,'bs')
plt.plot(x,y)

plt.plot(x1,y1,'ro')
plt.plot(x1,y1)

plt.xlabel("distance X")
plt.ylabel("H Tan0")