print("welcome to the world of beyblading")
print("the main protaganist beyblade series is tyson granger and his friend dragoon")
print("the main protaganist in beybvlade metal series is gingka hagane and his friend storm pegasus")
a=10
print("value: ",a,type(a),id(a))
b=20
print("value: ",b,type(b),id(b))
c=a+b
print("addition of the values: ",c,type(c),id(c))
x=float(a) # it's is a type cast.
print("value of 'x' : ",x)
y=complex(b) # it coverts int to complex value.
print("value of 'y' : ",y,type(y),id(y))
# variable as string.
sport='beyblade'
print("sport: ",sport)
print("static merge string: ",sport+' world')
print("individual characters with +ve index values: ",sport[0],sport[3],sport[7],sport[1],sport[5],sport[2])
'''  that means the above string 'beyblade' is divided as an array. that means
above the string it has negative index values and
below the string it has positive index values
negative index values:  -8  -7  -6  -5  -4  -3  -2  -1
the string is        :   b   e   y   b   l   a   d   e
positive index values:   0   1   2   3   4   5   6   7   '''
print("individual characters with -ve values: ",sport[-1],sport[-2],sport[-6],sport[-4])
print("strings: ",sport[0:2],sport[1:4],sport[3:5],sport[3:6],sport[0:3],sport[3:8])
# ex:- take sport[0:2] that means it prints 1st position of 0 and then it prints 2 means first two characters.
print("string are: ",sport[0:],sport[:8],sport[2:],sport[-4:])
print("result: ",'my '+sport[-5:],len(sport))