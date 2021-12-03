'''
lottery ticket using linear search
'''

a = []
n = int(input("enter no of tickets: "))
found = 0
for i in range(1, n + 1):
    p = int(input(f"enter the ticket number{i}: "))
    a.append(p)

print("the ticket numbers are: ", *a)
key = int(input("enter the ticket number to be search: "))
for i in range(1, n + 1):
    if a[i] == key:
        print(f"the ticket {a[i]} is found at position: ", i)
        found = 1
        break

    if found >= 1:
        print("congratulations you have won the lottery")
    else:
        print("ticket number is not found")

print("end of the program")