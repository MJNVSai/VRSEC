# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 17:39:38 2021

@author: Krishna
"""



from scipy import stats

estimates = [1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
print("items in a list: ")
for j in estimates:
    print(j)
    
print()
estimates.sort()
print("items in list acendending order: ")
for i in estimates:
    print(i)
    
# to find trimmed mean of the list
tm = stats.trim_mean(estimates,0.1)
# 0.1 means 10%
print("mean of list: ",tm)