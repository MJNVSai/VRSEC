# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:23:34 2021

STRING OPERATIONS

@author: Krishna
"""

#import string

s = "Raj"
print("lowered string characters is: ",s.lower())
print("uppered string characters is: ",s.upper())
print()

sl = list(s) #sl means string list
print("sting characters converted into list are: ",sl)

print("replacing the characters: ",s.replace("j", "#"))
print("replacing the characters: ",s.replace("aj","#"))
print("replacing the characters: ",s.replace("Ra","#"))
print("replacing the characters: ",s.replace("ra","#"))
print("replacing the characters: ",s.replace("Ra","*#"))
print("replacing the characters: ",s.replace("a","*#"))
print()

print("string list: ",sl)

l = ["a","b","c","d","e","f"]

print("half string_1: ",l[1:4])
print("half string_2: ",l[:4])
print("half string_3: ",l[2:])
print("full string is: ",l[:])

print("index of characters 'd' is: ",l.index('d'))

