'''
OVERLOADING THE 'IN' OPERATOR
'''

class overload:
    def __init__(self):
        self.numbers = [1,2,3,4,54]
    def __contains__(self, item):
        return item in self.numbers

obj1 = overload()
print("checking the number: ",56 in obj1)
print("checking another number: ",3 in obj1)
