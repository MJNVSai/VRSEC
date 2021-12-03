# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:00:32 2021

@author: Krishna
"""

import random



while True:
    year = random.randint(1993,2021)
    
    if year%4 == 0 and year%100!=0 or year%400 == 0:
        print(year,"===>","is a leap year")
    else:
        print(year,"===>","not a leap year")
        
    i = int(input("enter to continue with 1 or stop with 0: "))
    if i!=1:
        break

    