# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:09:04 2021

@author: Krishna
"""

import string
dict = {}
data = ""

file = open("output_data.txt","w")

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i-1]
print("converted dictionary: \n",dict)

with open("input_data.txt") as f:
    while 1:
        c = f.read(1)
        
        if not c:
            print(" End Of File ")
            break
        
        if c in dict:
            data = dict[c]
        else:
            data = c
        
        file.write(data)
        print(data,end = "")

file.close()
print()
print(" Documentation in the code is: ")
print(__doc__)