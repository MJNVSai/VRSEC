# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:40:55 2021

@author: Krishna
"""

with open("file1.txt","r+") as myfile:
    # here 'r' means only read mode
    # here 'r+' means you can read the file and write the file also
    print(myfile.read())
    myfile.write(" I am Fine Here Bro.\n")
# after opening the file must close the file after the work

myfile.close()