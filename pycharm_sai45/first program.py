print("PYTHON PROGRAM")
print("===========================")
# it is a single line comment
# to get all built in functions in python
print(dir(__builtins__))
print(dir(abs)) # yu will get the  sytax of that function.
print(dir(list))
print(dir(print))
a=10
b=20
c=30;d=40;e=40
''' 2 instructions in one line '''
print("the values are :",a,b)
# out is: the values are: 1020
a="kumar"
print("length of the static string: ",len(a))
print("the values are :",a,b)
# out is : the values are kumar20
# it will reduce the space used by the program.
if c>d:
    print("c is greater than d")
else:
    print("d is greater than a c")
# in python logical or is represented by 'or'.
if d==e or e==d:
    print("c is equal to the d")
else:
    print("c is not equal to the d")
