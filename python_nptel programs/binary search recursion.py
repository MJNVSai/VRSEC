# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 14:10:20 2021

BINARY SEARCH BY USING RECURSION CONCEPT

@author: Krishna
"""

def binary_search(l,x,start,end):
    # base case or anchor case: 1 element
    if start == end:
        if l[start] == x:
            return start
        else:
            return -1
    else:
        # dividing the array into 2 halves
        
        mid = (start + end)//2
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            # right half of array will be discarded
            
            return binary_search(l, x, start, mid-1)
        else:
            # left half will be discarded
            
            return binary_search(l, x, mid+1, end)
        
l = [90,10,100,45,87,34,29,68,99,42,23,1,95,9,98,8]
l.sort()
x = int(input("enter the number to search: "))
index = binary_search(l, x, 0, len(l)-1)

if index == -1:
    print(x,"is not found")
else:
    print(x,' is found at position ',index+1)
    
''' for human convinence we add the +1 to the index and print it is as result '''