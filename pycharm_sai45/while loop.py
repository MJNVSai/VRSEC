# topic while loop :
# while loop
# nested while loop
# while else
i = 1
while i <= 100 :
    print('welcome to the while loop\n',i)
    i += 1
print('while loop')

i1 = 10
while i1 <= 50 :
    print(i1,end = "+")
    i1 += 1

n = 0
while n!=1 :
    print('you are in the while loop')
    print('press 1 to exit from the loop: ')
    n = int(input())
print('now! yu are out of the while loop')

s = 1
while s!=0 :
    s = int(input('enter a number: '))
    print('square of the given number: ',s*s)
    print('to come out of the while loop enter 0')
print('end of the while loop')

# to find factorial of the number
i =1
fact =1
n1 = int(input('enter any number: '))
while i<=n1 :
    fact *= i
    i += 1
print('factorial of',n1,'is',fact)

# while loop with string
string = input('enter any word or string: ')
i4 = 0
while i4<len(string) :
    print(string[i4])
    i4 += 1
print('end of while loop')

# while loop with list
avengers = ['captain america','iron man','black widow','spider man']
w = 0
while w<len(avengers) :
    print(avengers[w])
    w += 1
print('end of while loop')

# nested while loop
i10 = 1
while i10<=5 :
    print('rocking  ',end="")
    j10 = 1
    while j10<=4 :
        print('star ',end="")
        j10 += 1
    i10 += 1
    print()


# while loop with else
t = 1
while t<=5 :
    print(t)
    t += 1
else :
    print('this is a else block or part')


num = 1
while num<=5 :
    print(num,'is less than 5')
    num += 1
else :
    print('we reached to number 5')