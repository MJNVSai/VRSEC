# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 13:09:15 2021

FACTORIAL WITH OUT USING RECURSION

@author: Krishna
"""

def factorial(n):
    product = 1
    
    for i in range(1,n+1):
        product *= i
    
    return product

n = int(input("enter a positive number: "))

if n < 0:
    print("factorial is not defined for negative numbers")
else:
    f = factorial(n)
    print("factorial of",n,"is: ",f)