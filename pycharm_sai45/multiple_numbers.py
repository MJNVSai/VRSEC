'''
searching multiple numbers using linear search
'''

n = int(input("enter the no.of elements: "))
a = []
found = 0

for i in range(0,n):
    p = int(input("enter a number: "))
    a.append(p)

key = int(input("enter a search element: "))
for i in range(0,n):
    if a[i] == key:
        print(key,"element is present at location: ",i)
        found += 1

if found == 0:
    print("element is not found")

print("end of the program")