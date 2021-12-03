# for loop is used for sequential traversal¶
# it can be used for traverse string or array
# iterating over a squence is called traversal
# range( ) :-
# this function is used for to generate sequence of the numbers
# sequence of the range function is range(start,end,step_size)
# default value of the step size is 1
for x in range(5,11) :
    print(x)
for x1 in range(5,26,2) :
    print(x1)
# for loop with string
print('for loop with string')
string = input('enter any string: ')
for x2 in string :
    print(x2)
string1 = 'tyson granger'
for x3 in string1 :
    print(x3)
# for loop with list
print('for loop with list')
student = ['ravi','mounav','prabhuram','sai','bhargav']
for x4 in student :
    print(x4)
# multiplication of the any table
print('multiplication of the any table')
number = int(input('enter any integer value: '))
print(number,'table: ')
for x5 in range(1,21) :
    print(number,'*',x5,'=',number*x5)
# for loop with else is possible
for name in ['parents','friends','problems','solutions'] :
    print(name)
else :
    print('for loop is ended')
for s in ['acer','hp','lenovo',5,10,2.3,2] :
    if s == 10 :
        break
    else :
        print(s)
else :
    print('this is else block')
# square of the numbers
print('square of the numbers')
for x6 in range(1,21,1) :
    print('square of',x6,'is',x6*x6)
# print even numbers
print('even numbers: ')
for y in range(1,51) :
    if y%2==0 :
        print(y)
# print even numbers using range of function
for y1 in range(0,51,+2) :
    print(y1)
# print odd numbers using range of function
for y2 in range(1,51,2) :
    print(y2)
z1 = int(input('enter an integer: '))
for z in range(z1) :
    print(z)
# to print reverse of the numbers
print('to print reverse of the numbers')
for z2 in range(100,0,-1) :
    print(z2)
# sum of numbers using list
print('sum of numbers using list')
n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sum = 0
for n1 in n :
    sum += n1
print(sum)