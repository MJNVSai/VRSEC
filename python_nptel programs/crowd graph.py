# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 18:54:51 2021

@author: Krishna
"""

import statistics

import matplotlib.pyplot as plt
estimates = [1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
y = []

estimates.sort()
tm = int(0.1*(len(estimates)))
estimates = estimates[tm:]
estimates = estimates[:len(estimates)-tm]
for i in range(len(estimates)):
    y.append(5)
    
    
plt.plot(estimates,y,'r--')

plt.plot([statistics.mean(estimates)],[5],'ro')

plt.plot([statistics.median(estimates)],[5],'bs')

plt.plot([375],[5],'g^')

print("statistics.mean(estimates): ",statistics.mean(estimates))
print("statistics.median(estimates): ",statistics.median(estimates))