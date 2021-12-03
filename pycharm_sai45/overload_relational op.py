'''
OVERLOADING THE RELATIONAL OPERATRORS
'''

class overload:
    def __init__(self,a):
        self.a = a
        print("this is constructor block\n")

    def __lt__(self, other):
        print("THIS is overloaded less than(<) operator block\n")
        if self.a < other.a:
            return True
        else:
            return False

    def __gt__(self, other):
        print("This is overloaded greater than(>) operator block\n")
        if self.a > other.a:
            return True
        else:
            return False

    def __le__(self, other):
        print("This is overloaded (<=) operator block\n")
        if self.a <= other.a:
            return True
        else:
            return False

    def __ge__(self, other):
        print("This is overladed (>=) operator block\n")
        if self.a >= other.a:
            return True
        else:
            return  False

    def __eq__(self, other):
        print("This is overloaded (==) operator block\n")
        if self.a == other.a:
            return True
        else:
            return False

    def __ne__(self, other):
        print("This is overloaded (!=) operator block\n")
        if self.a!=other.a:
            return True
        else:
            return False

obj1 = overload(int(input("enter first number: ")))
obj2 = overload(int(input("enter second number: ")))

obj3 = obj1 < obj2
obj4 = obj2 > obj1
obj5 = obj1 <= obj2
obj6 = obj1 >= obj2
obj7 = obj1 == obj2
obj8 = obj1!=obj2

print(" < operator overloaded in objects: ",obj3)
print(" > operator overloaded in objects: ",obj4)
print(" <= operator overloaded in objects: ",obj5)
print(" >= operator overloaded in objects: ",obj6)
print(" == operator overloaded in objects: ",obj7)
print(" != operator overloaded in objects: ",obj8)








