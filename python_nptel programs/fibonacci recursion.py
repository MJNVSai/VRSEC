# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:32:31 2021

FIBONACCI SERIES USING RECURSION

@author: Krishna
"""

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return (fib(n-1) + fib(n-2))

x = int(input("enter a number: "))
print("fibonacci series upto",x,": ")

for i in range(x):
  print(fib(i),end = ",")