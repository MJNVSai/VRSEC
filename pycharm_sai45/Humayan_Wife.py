'''
Finding the Humayan's wife using binary search method.....
'''

# Binary search
n = int(input("Enter the total number of jails in Humayun's Place: "))
b = []

for i in range(n):
    p = int(input("enter jail number{}: ".format(i + 1)))
    b.append(p)

# print("list: ",b)
key = int(input("Enter the clue given by Humayun: "))

found = 0
high = n
low = 1

while low <= high and found == 0:

    mid = (high + low) // 2

    if b[mid] == key:
        # print(key,"is present at location ",mid)
        found = 1

    elif key < b[mid]:
        high = mid - 1

    elif key > b[mid]:
        low = mid + 1

if found != 0:
    print("Hurray!The King rescued the Queen")
else:
    print("The King has been fooled by Humayun")