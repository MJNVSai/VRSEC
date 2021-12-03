# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 10:29:06 2021

@author: Krishna
"""

# to draw the graph of the LCR circuit
import matplotlib.pyplot as plt

f = [s for s in range(4,25,1)]
# here values of 'f' are frequencies

r200 = [2.02,2.35,2.62,3.18,4.36,5.20,6.71,8.31,10.42,12.26,13.75,12.13,10.96,8.98,7.51,6.02,5.18,4.37,3.98,3.44,3.14]
# r200 is the resistance of 200 ohms  for current

r500 = [1.74,2.15,2.75,3.40,3.78,4.65,5.85,6.61,7.36,7.60,7.85,7.32,6.68,6.08,5.56,5.05,4.32,3.92,3.57,3.19,2.85]
# r500 is the resistance of 500 ohms for current

plt.plot(f,r200,"ro")
plt.plot(f,r200)

plt.plot(f,r500,'bs')
plt.plot(f,r500)

plt.xlabel('frequency in HZ')
plt.ylabel('current in mA')