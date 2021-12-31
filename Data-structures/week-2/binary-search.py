'''
We have discussed Binary search algorithm in the class. Implement the same algorithm using any of the languages like C/Python. Write all the possible testcases. Write down your observations. 
Sample input
Enter number of elements 8
Enter 8 elements
44,16,18,164,47,10,0,-68
Enter element to search 10
Sample output
10 is present at location 5
'''

# Program:
n = int(input("enter length of the array: "))
b = []

for i in range(n):
    p = int(input("enter element{}: ".format(i + 1)))
    b.append(p)

# print("list: ",b)
key = int(input("enter the search element: "))

found = 0
high = n - 1
low = 0

# print("values are: ",high,low,mid)

while low <= high and found == 0:

    mid = (high + low) // 2

    if b[mid] == key:
        print(key, "is present at location ", mid)
        found = 1

    elif key < b[mid]:
        high = mid - 1

    elif key > b[mid]:
        low = mid + 1

'''
Output:

enter length of the array: 8
enter element1: 44
enter element2: 47
enter element3: 59
enter element4: 76
enter element5: 98
enter element6: 110
enter element7: 116
enter element8: 118
enter the search element: 98
98 is present at location  4
'''
