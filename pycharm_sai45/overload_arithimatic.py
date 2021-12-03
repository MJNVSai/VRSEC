'''
overloading the Arithimatic operators
'''

class overload:
    def __init__(self,a):
        self.a = a
        print("this is constructor block\n")

    def __add__(self, other):
        print("This is overloaded ADD(+) block\n")
        return self.a + other.a

    def __sub__(self, other):
        print("This is overloaded sub(-) operator block\n")
        return self.a - other.a

    def __mul__(self, other):
        print("This is overloaded mul(*) operator block\n")
        return self.a * other.a

    def __truediv__(self, other):
        print("This is overloaded divison(/) operator block\n")
        return self.a / other.a

    def __pow__(self, power):
        print("This is overloaded power(**) operator block\n")
        return self.a ** power.a

    def __mod__(self, other):
        print("This is overloaded modulo(%) operator block\n")
        return self.a % other.a

    def __floordiv__(self, other):
        print("This is overloaded floor division(//) operator block\n")
        return  self.a // other.a

obj1 = overload(3)
obj2 = overload(2)

obj3 = obj1 + obj2
obj4 = obj1 - obj2
obj5 = obj1 * obj2
obj6 = obj1 / obj2
obj7 = obj1 ** obj2
obj8 = obj1 % obj2
obj9 = obj1 // obj2

print(" + operator overloaded in objects: ",obj3)
print(" - operator overloaded in objects: ",obj4)
print(" * operator overloaded in objects: ",obj5)
print(" / operator overloaded in objects: ",obj6)
print(" ** operator overloaded in objects: ",obj7)
print(" % operator overloaded in objects: ",obj8)
print(" // operator overloaded in objects: ",obj9)