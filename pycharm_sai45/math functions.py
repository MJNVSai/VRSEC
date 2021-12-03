# Math functions
help('math')
# Square root function
import math
x = math.sqrt(285)
print('sqrt of 285: ',x)
x1 = math.sqrt(8)
print('sqrt of 8: ',x1)
# Power of function
y = math.pow(2,5) # returns 2^5
print('exponent power of 2 to 5: ',y)
y1 = math.pow(32.5,100)
print('exponent power of 32.5 to 100: ',y1)
# Ceil function
import math
a = float(input('enter first decimal value: '))
a1 = math.ceil(a)
print("ceil value: ",a1)
# Floor function
b = float(input('enter first decimal value: '))
b1 = math.floor(b)
print('floor value: ',b1)
# constant values
import math as s # yu can give any variable in place of 's' also.
c = s.pi
print("value of pi: ",c)
d = s.e
print('value of e or eplsilon: ',d)
print('type of epsilon: ',type(d))
# factorial function
e = int(input('enter first integer value: '))
e1 = s.factorial(e)
print('factorial value: ',e1,'\n type of factorial: ',type(e1))
# gcd function
f = int(input('enter first integer value: '))
f1 = int(input('enter second integer value: '))
f2 = s.gcd(f,f1)
print('gcd of two values: ',f2)
# if yu want to use only some functions in math module
# from math import function names
from math import isqrt,sqrt,pow
z = int(input('enter first integer value: '))
z1 = math.isqrt(z)
print('returns integer part of square root value: ',z1)
z2 = int(input('enter first integer value: '))
z3 = math.sqrt(z2)
print('returns float value of the square root value: ',z3)
v = int(input('enter first integer value: '))
v1 = int(input('enter second integer value: '))
v2 = math.pow(v,v1)
print('power raised to one value: ',v2)
import math as m
q = int(input('enter first integer value: '))
w = int(input('enter first integer value: '))
q1 = m.ldexp(q,w)
print('returns q*(2**w): ',q1)
# trigonometric functions
g1 = int(input('enter the angle value: '))
g2 = m.sin(g1)
print('sin(g1): ',g2)
d1 = int(input('enter the angle value: '))
d2 = m.cos(d1)
print('cos(d1): ',d2)
t1 = int(input('enter the angle value: '))
t2 = m.tan(t1)
print('tan(t1): ',t2)
# log10 function
s = int(input('enter first integer: '))
s1 = m.log10(s)
print('result: ',s1)