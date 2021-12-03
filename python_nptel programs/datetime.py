# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:47:15 2021

@author: Krishna
"""

import datetime
n = datetime.date.today()
print("today's date is: ",n)
print()

y = datetime.date.today().strftime("%Y")
print("today's year: ",y)
print()

m = datetime.date.today().strftime("%B")
print("today's  month string: ",m)
print()

d = datetime.date.today().strftime("%d")
print("today's date is: ",d)
print()

x = datetime.date.today().strftime("%W")
print("week number of the month: ",x)
print()

y = datetime.date.today().strftime("%w")
print("week day of the week is : ",y)
print()

dy = datetime.date.today().strftime("%j")
print('day of the year: ',dy)
print()

dw = datetime.date.today().strftime("%A")
print('day of the week: ',dw)
print()

s = datetime.datetime.now()
print("full date and time: ",s)
print()