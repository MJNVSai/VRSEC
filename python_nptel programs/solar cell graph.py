# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 13:31:18 2021

@author: Krishna
"""

# to draw the graph of solar cell
import matplotlib.pyplot as plt

r = [0,2,4,6,8,10,20,30,40,50,60,70,80,90,100,110]
# here r is the resistance or load

p = [1950,2220,2550,3150,3300,3335,3190,2720,2380,2100,1942.5,1710,1520,1365,1267.5,1200]
# here p is the power that means it is the product of voltage and current

plt.plot(r,p,'ro')
plt.plot(r,p)

plt.xlabel("resistance's (r)")
plt.ylabel("power (p) ")