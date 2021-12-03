# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:03:23 2021

@author: Krishna
"""

def fizzbuzz(r,p,q):
    for i in range(1,r+1):
        if i%p == 0 and i%q == 0:
            print(str(i) + "=" + "FizzBuzz")
        else:
            if i%p == 0:
                print(str(i) + "=" + "Fizz")
            else:
                if i%q == 0:
                    print(str(i) + "=" + "Buzz")
                else:
                    print(str(i))




a = int(input("enter the number to get fizz: "))
b = int(input("enter the number to get buzz: "))
c = int(input("enter the number to end the game: "))
print()
print("fizz and buzz numbers are: ",a,b)
print("game will be end with number: ",c)
print()
fizzbuzz(c,a,b)