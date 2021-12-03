# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:23:00 2021

@author: Krishna
"""

# magic square is only possible for only odd numbers
def magic(n):
    magicsquare = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0)
        magicsquare.append(a)
    
    # step 1: for position of '1' in magic square
    i = n//2
    j = n-1
    
    num = n**2
    count = 1
    
    while count <= num:
        # step 5
        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            # step 3
            if j == n:
                j = 0
            
            if i < 0:
                i = n - 1
        
        # step 4
        if (magicsquare[i][j]!=0):
            j = j - 2
            i = i + 1
            continue
        
        else:
            magicsquare[i][j] = count
            count = count + 1
            
        # step 2 : p - 1, p + 1
        i = i - 1
        j = j + 1
        
    # printing the magic square
    for i in range(n):
            for j in range(n):
                print(magicsquare[i][j], end = " ")
            print()
            
    # the magic number is M
    M = (n*(n**2 + 1))/2
    print("the sum of each row/column/diagonal is: ",M)
        
        
p = int(input("enter the order of the magic square in one number: "))
magic(p)