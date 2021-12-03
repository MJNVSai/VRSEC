# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 10:14:57 2021

@author: Krishna
"""

# compound pendulam's graph
import matplotlib.pyplot as plt

d = [x for x in range(5,100,10)]
# here d is  the distance from same end

t = [1.55,1.6625,1.16125,1.65,2.725,2.0875,1.55,1.6625,3.025,1.5125]
# here t is the time period

plt.plot(d,t,'bs')
plt.plot(d,t)

plt.xlabel('distance from same end')
plt.ylabel('time period in seconds')