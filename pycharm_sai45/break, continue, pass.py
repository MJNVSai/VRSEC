# Break statement :
# when we execute break statement it can terminate the current loop
# it is most probably use in for loop,while loop,if loop.
# with out using the break statement
for i in range(1,101) :
    print(i,end = ' @ ')

# using the break statement
for i1 in range(1,101) :
    if i1==98 :
        break
    else:
        print('\n',i1,end = ' $ ')

s = 'all python program'
for letter in s :
    if letter == 'p' or letter == 'o' :
        break
    else :
        print(letter)
print('out of the loop')

# candy program
total = 5
x = int(input('enter how many candies yu want: '))
i2 = 1
while i2 <= x :
    if i2 > total :
        print('out of the stock')
        break
    print('candy',i2)
    i2 += 1
print(" $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ")

# continue statement :¶
# it is used to skip the next statement and continue the loop
for y in range(1,11) :
    if y == 5 :
        continue
    else :
        print(y,end = ' * ')

for y1 in range(1,11) :
    if y1 >= 5 :
        continue
    else :
        print(y1,end=' @ ')

for y2 in range(1,11) :
    if y2 <= 5 :
        continue
    else :
        print(y2,end=' @ ')

for y3 in range(1,11) :
    if y3!= 5 :
        continue
    else :
        print(y3,end=' @ ')

# square of the number
while 1 :
    print('\n enter a number (<=100) to find its square: ')
    print('press 0 to exit: ')
    num = int(input())
    if num == 0 :
        print('program\'s end , thank you')
        break
    elif num >= 100 :
        print('number is greater than 100. try again')
        continue
    print('\n square of',num,'is',num**2)

# pass statement:
# when pass statement is executed, nothing happens, but yu avoid getting an error when empty code is not allowed
for z in range(1,101) :
    if z%2!=0 :
        pass
    else :
        print(z,end= ' % ')

for z in range(10) :
    pass
print('bye-------')

for z1 in range(5) :
    if z1 == 3 :
        pass
    else :
        print('number is ',z1)

list = ['a','b','c','d']
for l in list :
    if l == 'a' :
        pass
    else :
        print(l,end= ' ~ ')