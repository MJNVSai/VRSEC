t = input("enter the type of vehicle as a character: ")
time = int(input("enter the no.of hours for parking: "))

if t == 't' or t == 'b':
    print("parking charges: ",time*20)
elif t == 'c':
    print('parking charges: ',time*10)
elif t == 's' or t == 'c' or t == 'm':
    print('parking charges: ',time*5)
else:
    print(" input error ")