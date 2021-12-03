# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:37:30 2021

MATRIX ARITHIMATIC CALCULATIONS

@author: Krishna
"""

import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype = np.float64)

'''
matrix arithimatic using normal operators

'''
print("matrix addition: \n",x + y)
print("matrix subraction: \n",x - y)
print("matrix multiplication: \n",x*y)
print("matrix division: \n",x/y)

print()

'''

matrix arithimatic using inbuilt functions

'''
print("\nmatrix addition: \n",np.add(x,y))
print("\nmatrix subraction: \n",np.subtract(x,y))
print("\nmatrix multiplication: \n",np.multiply(x,y))
print("\nmatrix division: \n",np.divide(x,y))

print("\nsquare root of matrix A: \n",np.sqrt(x))
print("\nsquare root of matric B: \n",np.sqrt(y))

print("\nsum of all elements in matrix A: \n",np.sum(x))
print("\ntranspose of the matrix A: \n",x.T)

print("\nsum of the colums matrix A: ",np.sum(x,axis=0))
print("sum of elements in each row is matrix A: ",np.sum(x,axis=1))