# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 19:59:48 2021

NUMERICAL PYTHON MODULE

@author: Krishna
"""

import numpy as np

a = np.array([1,2,3,4,5,6])

print("data type of the variable a: ",type(a))

print("order of the given matrix: ",a.shape)
#a.shape returns first no.of colums and  then no,of rows only

print("elements in matrix: ",a[0],a[1],a[2])

a[0] = 100

print("first element in matrix is : ",a[0])