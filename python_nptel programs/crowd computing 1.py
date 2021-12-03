# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:12:16 2021

@author: Krishna
"""

from statistics import mean
estimates = [1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
print("items in a list: ")
for j in estimates:
    print(j)
    
print()
estimates.sort()
print("items in list acendending order: ")
for i in estimates:
    print(i)
    
# to find trimmed mean.
tm = int(0.1*len(estimates)) # 0.1 means 10%
print()
print("trimmed mean of the list: ",tm)

# to remove first 10% of smallest items in list
estimates = estimates[tm:]
print()
print("removal of 1st 10% smallest items: ")
for i1 in estimates:
    print(i1)
    
# to remove first 10% of largest items in a list
estimates = estimates[:len(estimates)-tm]
print()
print("removal of 1st 10% largest items: ")
for i2 in estimates:
    print(i2)

# now to find mean of the estimates
print()
print("mean of the list: ",mean(estimates))