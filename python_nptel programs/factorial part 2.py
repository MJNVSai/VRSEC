# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 13:15:19 2021

FACTORIAL BY USING RECURSION CONCEPT

@author: Krishna
"""

def fact(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    elif n > 1:
        return n*fact(n-1)
    
n = int(input("enter a non negative integer: "))

if n < 0:
    print("factorial is not defined for negative numbers")
else:
    print("factorial of {} is: {}".format(n,fact(n)))
    
    
''' It is a guard against a stack overflow, yes. Python (or rather, the CPython implementation) doesn't optimize tail recursion, and unbridled recursion causes stack overflows. You can check the recursion limit with sys.getrecursionlimit:

import sys
print(sys.getrecursionlimit())
and change the recursion limit with sys.setrecursionlimit:

sys.setrecursionlimit(1500)
but doing so is dangerous -- the standard limit is a little conservative, but Python stackframes can be quite big. '''

print(__doc__)