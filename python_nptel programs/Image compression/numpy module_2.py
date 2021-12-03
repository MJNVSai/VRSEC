# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:13:57 2021

numpy part 2

@author: Krishna
"""

import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])

print("shape of the matrix: ",a.shape)

b = a.shape 

print("colums and rows in matrix are: ",b[0],b[1],sep=",")  

x = np.zeros((2,5))
# 2 ===> no.of colums and 5 ===> no.of rows

print("zero matrix is: ")
print(x)

y = np.ones((5,10))
# 5 ===> rows and 10 ===> colums
print("unit matrix: \n",y)

z = np.full((4,4),6)
#here 6 ===> is the fill number in the matrix
print("matrix of all elements with 6: \n",z)

z1 = np.random.random((3,2))
print("random matrix is : \n",z1)