'''
Suppose you are implementing Linear search algorithm using any of the languages like C/Python. In the given array if there is a possibility of multiple occurances of some elements. In such case how to identify the location of the element. Design and implement the solution for the same.
Sample input
Enter number of elements 6
Enter 6 elements
44,16,18,16,47,16
Enter element to search 16
Sample output
16 is present at location 1
16 is present at location 3
16 is present at location 5
'''

# Program:
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

if found == 0:
    print("element is not found")

print("end of the program")

'''
Output:
enter the no.of elements: 5
enter a number: 1
enter a number: 9
enter a number: 2
enter a number: 2
enter a number: 1
enter a search element: 1
element is present at location:  0
element is present at location:  4
end of the program
'''
