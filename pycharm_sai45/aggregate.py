a = int(input("enter your roll number: "))
print("student roll number: ",a)


print(" enter the subject marks ")
b1 = float(input("enter the marks of english: "))
b2 = float(input("enter the marks of BEE: "))
b3 = float(input("enter the marks of c programming: "))
b4 = float(input("enter the marks of peripherals: "))

sum = b1 + b2 + b3 + b4
print("total of subjects: ",sum)



agg = (sum/400)*100
print("aggregate percentage: ",agg)

if agg >= 75:
    print(a,' = distinction')
elif 60 <= agg < 75:
    print(a,' = first division')
elif 50 <= agg < 60:
    print(a,' = second division')
elif 40 <= agg < 50:
    print(a," = third division")
else:
    print(a," = fail")