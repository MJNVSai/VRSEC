# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 16:02:49 2021

week 4 programming assignment 3 arrangements

@author: M.J.N.V.Sai
"""

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = input().split()
s = list(map(int,n))
d = len(s)
i = s.count(1)
i1 = s.count(0)
ans = fact(d)//(fact(i)*fact(i1))
print(ans)


''' 
Sample Test Cases:
    
Input	Output:
    
Test Case 1:
0 1 0 1
test case 1 output
6

Test Case 2	
0 1 1 0 1
test case 2 outut
10

Test Case 3	
1 1 0 1 0 0 1 0 1 1
test case 3 output
210 '''