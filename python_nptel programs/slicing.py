# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 16:31:14 2021

@author: Krishna
"""

students = ["Arun","Harish","Akanksha","Rajesh","Varsha","Lakshmi"]
students.sort()
print(students)

students.insert(0,"JOC")
print(students)

# slicing starts
# syntax: list_name[start_index:end_index+1]

print("sub set of list: ",students[1:5])

print("no start and no end values: ",students[:])

print("only start value: ",students[3:])

print("only end value: ",students[:5])

# default start_index = 0
# default end_index = len(list)

print("sub set of list 2: ",students[2:5])