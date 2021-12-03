# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 14:56:54 2021

TO CHECK GIVEN STRINGS ARE ANAGRAMS OR NOT

@author: Krishna
"""

str1 = input("enter the first string: ")
str2 = input("enter the second string: ")

s1 = sorted(str1)
s2 = sorted(str2)

for i in s2:
    if i == " ":
        s = s2.index(i)
        s2.pop(s)

for i in s1:
    if i == " ":
        a = s1.index(i)
        s1.pop(a)
        

print("sorted first string: ",s1)
print("sorted second string: ",s2)

print()
if s1 == s2:
    print(" These are anagrams ")
else:
    print(" These are not anagrams ")
    