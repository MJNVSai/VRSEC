# here special operators means bitwise,membership,identity operators.
a=int(input("enter any one interger: "))
b=int(input("enter any one integer: "))
print("integers: ",a,b)
# 1. using bitwise operators in python.
print("a & b: ",a&b) # '&'===> bitwise AND.
print("a | b: ",a|b) # '|'===> bitwise OR.
print("a >> b: ",a>>b) # '>>'===> bitwise RIGHT SHIFT.
print("a << b: ",a<<b) # '<<'===> bitwise LEFT SHIFT.
print("a ^ b: ",a^b) # '^'===> bitwise XOR.
# 2. using membership operators in python.
# here sequence means list or tuple or set.
# membership opertors always returns 'boolean values'.
hero=[99,'tyson',200,'brooklyen',988.999,'kenta']
print("list is: ",hero, type(hero), id(hero), len(hero))
print("operator 'in': ",'tyson' in hero)
print("using operator 'in': ", 260 in hero)
# for operator 'in'===> it returns TRUE if it finds specified element in sequence otherwise returns FALSE.
print("using operator 'not in': ",988.999 not in hero)
print("using operator 'not in': ",'kai' not in hero)
# for operator 'not in'===>  it returns TRUE if it does't find specified element in sequence otherwise it returns FALSE.
# 3. using 'identity' operators.
x,y,z=100,100,99.9
print(x,y,z, type(x), type(y), type(z))
print("using operator 'is': ",x is y)
# for operator 'is'====>  it returns TRUE if both variables are the same object otherwise it returns FALSE.
print("using operator 'is': ",y is z)
print("using operator 'is not': ",x is not y)
# for operator 'is not'====>  it returns TRUE if both variables are not the same object otherwise returns FALSE.
print("using operator 'is not': ",x is not z)
# identity opertors always returns boolean values.
