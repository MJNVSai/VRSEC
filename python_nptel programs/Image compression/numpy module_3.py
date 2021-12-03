# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:29:46 2021

numpy part 3

@author: Krishna
"""

import numpy as np

x = np.array([1,2,3])
y = np.array([1.0,2.0])

print("data type of the x: ",x.dtype)
print("data type of the y: ",y.dtype)

z = np.array([5,4,10], dtype = np.int64)
# the above staement is forcing the array to use int64 bit storage
print("data type of the z: ",z.dtype)