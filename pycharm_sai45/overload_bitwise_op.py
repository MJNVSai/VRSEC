'''
OVERLOADING BITWISE OPERATORS
'''

class bitwise:
    def __init__(self,a):
        print("this is constructer block\n")
        self.a = a

    def __rshift__(self, other):
        print("this is overloading (>>) operator block\n")
        return self.a >> other.a

    def __lshift__(self, other):
        print("this is overloading (<<) operator block\n")
        return self.a << other.a

    def __and__(self, other):
        print("this is overloading (logical and) operator block\n")
        return self.a & other.a

    def __or__(self, other):
        print("this is overloading (logical or) operator block\n")
        return self.a | other.a

    def __xor__(self, other):
        print("this is overlaoding (logical ^) operator block\n")
        return self.a ^ other.a

obj1 = bitwise(int(input("enter 1st binary number: ")))
obj2 = bitwise(int(input("enter 2nd binary number: ")))

obj3 = obj1 >> obj2
obj4 = obj1 << obj2
obj5 = obj1 & obj2
obj6 = obj1 | obj2
obj7 = obj1 ^ obj2

print(" >> operator overloaded in objects: ",obj3)
print(" << operator overloaded in objects: ",obj4)
print(" and operator overloaded in objects: ",obj5)
print(" or operator overloaded in objects: ",obj6)
print(" ^ operator overloaded in objects: ",obj7)
