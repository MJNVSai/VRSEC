# concept if :
# if
# if else
# if else ladder
# Nested if
# if
x = int(input('enter the integer value: '))
if x>98 :
    print(x,'is greater number')
# to check given number is +ve or -ve or 0
x1 = int(input('enter the integer value: '))
if x1>0 :
    print(x1,'is positive(+ve) number')
if x1<0 :
    print(x1,'is negative(-ve) number')
if x1==0 :
    print(x1,'is neutral')
# if else
y = int(input('enter the integer value: '))
if y!=10 :
    print(y,'is less than 10')
else :
    print(y,'is greater than 10')
# to check eligible voter age
y0 = input('enter your name: ')
y1 = int(input('enter your age: '))
if y1 > 18 and y1 <= 120 :
    print(y0,'is eligible for election voting')
else :
    print(y0,'is not eligible for election voting')
# to check given number is even or odd
z = int(input('enter the integer value: '))
if z%2==0 :
    print(z,'is a even number')
else :
    print(z,'is a odd number')
# to check gender
name = input('enter your name: ')
gender = input('are you male(y): ')
if gender == 'y' or gender == 'Y' :
    print(name,'is a male')
else :
    print(name,'is a female')
# if else ladder
# student percentage
student = input('enter the student name: ')
percent = float(input('enter the student percentage: '))
if percent >= 75 and percent <= 100 :
    print(student,'belongs to first division')
elif percent >= 45 and percent < 75 :
    print(student,'belongs to second division')
elif percent >= 37 and percent < 45 :
    print(student,'belongs to third division')
else :
    print(student,'failed in the examination')
# to calculate bill amount
name1 = input('enter your name: ')
amount = float(input('enter bill amount: '))
if amount >= 5000 :
    amount = amount - 500
elif amount >= 4000 and amount <= 4999 :
    amount -= 400
elif amount >= 3000 and amount <= 3999 :
    amount -= 300
elif amount >= 2000 and amount <= 2999 :
    amount -= 200
elif amount >= 1000 and amount <=1999 :
    amount -= 100
print(amount,'is your final bill amount sir!')
# Nested if
# to find greatest value in the three numbers
print('enter any three numbers: ')
a = int(input('enter first number value: '))
b = int(input('enter second number value: '))
c = int(input('enter third number value: '))
if a>b :
    if a>c :
        print(a,'is greatest number')
if b>a :
    if b>c :
        print(b,'is greatest number')
if c>a :
    if c>b :
        print(c,'is greatest number')