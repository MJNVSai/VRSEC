a=int(input("enter an integer value 1: "))
print(type(a)) # type() means it's type of a variable
print(id(a)) # id() means it's address of a variable
b=int(input("enter an integer value 2: "))
print(type(b))
print(id(b))
print("addtion of values: ",a+b)
print("square of values: ",a*a,b*b)
print("subraction of values: ",a-b)
print("multiplication of values: ",a*b)
# * ==> single astrisk indicates the multiplication only.
print("float division of values: ",a/b)
# the float division gives result in float type only.
print("integer division of values: ",a//b)
# the second slash indicates the give result in integer type only.
print("remainder of values: ",a%b)
print("the power of first value to the second value: ",a**b) # or yu can use pow(a,b) also.
# ** ==> the double astrisk's indicates the power of (like 2^3=8).
# to find length of the string.
print("length of the string: ",len('sai'))
print("length of the string: ",len("beyblade"))
c='tyson granger '
d="beyblade dragoon metal strom "
print(c)
print(d)
print("length of the string: ",len(c))
print("length of the string: ",len(d))
print("same or equal strings: ",a*c)
# here it prints same string as 'a' times.
print("multiple strings: ",b*d)
# here it prints same string as "b" times
