# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 20:19:27 2021

spiaral square using turtle

@author: Krishna
"""

import turtle
from random import randint
turtle.bgcolor("black")
seurat = turtle.Turtle()

width = 10
height = 10

dot_distance = 25

seurat.penup()
list_colour = ["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]

seurat.setpos(-250,250)

def spiral(m,n):
    k = 0
    l = 0
    f = 0
    seurat.color("white")
    
    '''
    k = index of starting row
    l = index of starting column
    n = ending row index
    m = ending column index
    '''
    col = randint(0,10)
    seurat.color(list_colour[col])
    
    while k < m and l < n:
        
        if f == 1:
            seurat.right(90)
        # printing the first row from remainng rows
        for i in range(l,n):
            seurat.dot() 
            seurat.forward(dot_distance)
        
        k = k + 1
        f = 1
        
        seurat.right(90)
        
        col = randint(0,10)
        seurat.color(list_colour[col])
        
        #printing the last column from remainng column
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            
        n = n - 1
        seurat.right(90)
        
        col = randint(0,10)
        seurat.color(list_colour[col])
        
        if k < m:
            #printing the last row from remaing rows
            
            for i in range(n-1,l-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                
            m = m - 1
        
        seurat.right(90)
        
        col = randint(0,10)
        seurat.color(list_colour[col])
        
        if l < n:
            # printing the first column from the remainng columns
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                
            l = l + 1
            
            
spiral(20,20)
turtle.done()
        