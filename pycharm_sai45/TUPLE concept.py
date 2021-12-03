# concept "tuple".
a=(36,99,1,100,"yu tendo","hikaru hasama","mounav","ram",89.56,879.45,160.098)
print("static tuple: ",a,type(a), id(a))
# in tuple yu can't change the values or yu can't delete the values.
print(a[1],a[5],a[0:4],a[4:],a[:10],a[-3:-1])
print("index value: ", a.index(160.098), "\nlength of tuple: ",len(a)) # it returns 'index' value for a.index().
b=(12,"vamsi",28.9)
print(b, type(b))
print("first tuple: ",a, "\n second tuple: ",b)
print("merged tuple: ",a+b)
c=(100,98,45,68,6,99.99,56.76,20.987,-9,-6)
print("maximum value in tuple: ",max(c))
print("minimum value in tuple: ",min(c))
print("length of thrid tuple: ",len(c))
# conversion==>  from tuple to list.
print("first tuple: ",a,type(a))
print("conversion: ",list(a),type(list(a)))
# conversion===> from list to tuple.
d=[20,40,"ram","sai",89.76,98.89]
print("first list: ",d, type(d))
print("conversion: ",tuple(d),type(tuple(d)))
print("conversion from list to set: ",set(d),type(set(d)))
print(a.__add__(b))


