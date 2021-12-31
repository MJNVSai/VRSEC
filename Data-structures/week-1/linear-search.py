'''
We have discussed linear search algorithm in the class. Implement the same algorithm using any of the languages like C/Python. Write all the possible testcases. Write down your observations. 
Sample input
Enter number of elements 8
Enter 8 elements
44,16,18,164,47,10,0,-68
Enter element to search 10
Sample output
10 is present at location 5
'''

# Program
n = int(input("enter the no.of elements: "))
a = []
found = 0

for i in range(0,n):
    p = int(input("enter a number: "))
    a.append(p)

key = int(input("enter a search element: "))
for i in range(0,n):
    if a[i] == key:
        print("element is present at location: ",i)
        found += 1
        break

if found == 0:
    print("element is not found")

print("end of the program")

'''
Output:
enter the no.of elements: 5
enter a number: 9
enter a number: 1
enter a number: 87
enter a number: 76
enter a number: 3
enter a search element: 76
element is present at location:  3
end of the program
'''
