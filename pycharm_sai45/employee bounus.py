# to find the bonous of the employee

salary = int(input("enter the employee salary: "))
gender = input("enter the gender 'm' for male, 'f' for female: ")
print("normal salary of the employee: ",salary)

if gender == 'M' or gender == 'm':
    if salary <= 10000:
        bonus = salary*0.02 # 0.02 means 2%
        print("bonus on salary: ",bonus)
    else:
        bonus = salary*0.05 # 0.05 means 5%
        print("bonus on salary: ",bonus)
elif gender == 'F' or gender == 'f':
    if salary <= 10000:
        bonus = salary*0.2
        print("bonus on salary: ",bonus)
    else:
        bonus = salary*0.1 # 0.1 means 10%
        print("bonus on salary: ",bonus)
else:
    print("input error")

salary = salary + bonus

print("total salary of employee with bonus: ",salary)