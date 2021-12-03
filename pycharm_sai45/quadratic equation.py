i = int(input('first value: '))
j = int(input('second value: '))
k = int(input('third value: '))
d = (j**2) - (4*i*k)
r1 = (-j + (d**0.5))/(2*i)
r2 = (-j - (d**0.5))/(2*i)
if d>0 :
    print('roots are real: ',r1, r2, sep=" $$ ")
elif d<0 :
    print('roots are complex: ',r1, r2, sep=" $$ ")
else :
    print('roots are real and equal: ',(-j/(2*i))," and ",(-j/(2*i)))
print('code over')