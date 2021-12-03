# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:56:44 2021

searching and sorting

@author: Krishna
"""

def linear_search(n,x):
    element = []
    for i in range(1,n):
        element.append(i)
        
    count = 0
    flag = 0
    for i in element:
        count += 1
        if i == x:
            print("yes!! i found my number at position: ",i)
            flag = 1
            break
    
    if flag == 0:
        print("number",x,'is not found')
        
    print("number of iterations: ",count)
    

print()
print(" USING LINEAR SEARCH METHOD ")
e = int(input("enter a last number in your range: "))
f = int(input("enter a number to find: "))
linear_search(e, f)
    
    
def binary_search(a,x):
    first_pos = 0
    last_pos = len(a) - 1
    
    flag = 0
    count = 0
    
    while first_pos <= last_pos and flag == 0:
        count += 1
        mid = (first_pos + last_pos)//2
        
        if x == a[mid]:
            flag = 1
            print("the element is present at position: ",mid)
            print("the number of iterations are: ",count)
            return
        else:
            if x < a[mid]:
                last_pos = mid - 1
            else:
                first_pos = mid + 1
    
    print("the number is not present")
    
    
print()
print(" USING BINARY SEARCH METHOD ")
a = []
s = int(input("enter the last number in your range of numbers: "))
m = int(input("enter your number to find or not find: "))
for i in range(1,s+1):
    a.append(i)
    
binary_search(a, m)