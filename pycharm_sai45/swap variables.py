# decimal conversions.
# Decimal to binary conversion:
# bin() ==> it converts decimal to binary number.
a = int(input('enter the decimal number: '))
print('decimal value: ',a,'\n type of decimal value: ',type(a))
b = bin(a)
print('binary of decimal : ',b,'\n type of binary: ',type(b))
help(bin)
# Decimal to octal conversion:
# oct( )===> it converts decimal to octal number
c = int(input('enter the decimal value: '))
print('decimal value: ',c,'\n type of decimal: ',type(c))
d = oct(a)
print('octal of the decimal: ',d,'\n type of octal: ',type(d))
help(oct)
# Decimal to hexadecimal:¶
# hex( )====> it converts decimal to hexadecimal number
e = int(input('enter the decimal number: '))
print('decimal number: ',e,'\n type of decimal: ',type(e))
f = hex(e)
print('hexadecimal of decimal: ',f,'\n type of hexadecimal: ',type(f))
help(hex)
# Swapping of numbers by using third variable.
g = int(input('enter the integer value: '))
h = int(input('enter the integer value: '))
print('the values before swapping: ',g, h)
t = g
g = h
h = t
print('the values after swapping: ',g, h)
print('type of values: ',type(g), type(h))
# Swapping of the numbers without using third variable.
i = int(input('enter the integer value: '))
j = int(input('enter the integer value: '))
print('values before swapping: ',i, j)
i = i + j
j = i - j
i = i - j
print('values after the swapping: ',i, j)
print('type of the values: ',type(i), type(j))
# One line swapping.
k = int(input('enter the integer value: '))
l = int(input('enter the integer value: '))
print('values before swapping: ',k, l)
k,l = l,k
print('values after swapping: ',k,l)
print('type of values: ',type(k), type(l))
# Swap by using XOR operator
# ^ ===> this is the symbol of the XOR operator
m = int(input('enter integer value: '))
n = int(input('enter integer value: '))
print('values before swapping: ',m, n)
m = m ^ n
n = m ^ n
m = m ^ n
print('values after swapping: ',m, n)
print('type of values: ',type(m), type(n))


