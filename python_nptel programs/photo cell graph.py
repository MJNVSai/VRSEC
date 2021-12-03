# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 18:21:30 2021

@author: Krishna
"""

# to draw the graph of the photo cell
import matplotlib.pyplot as plt
# values for voltage and high intensity
plt.plot([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30],[6,22,32,42,52,58,60,60,60,58,59,59,55,58,60,58])

# values for voltage and medium intensity
plt.plot([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30],[4,20,30,40,50,56,58,56,56,58,58,59,56,58,58,60])

# values for voltage and low intensity
plt.plot([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30],[2,18,28,38,43,45,46,46,46,48,48,49,48,50,50,50])

plt.xlabel("voltages")
plt.ylabel("currents")