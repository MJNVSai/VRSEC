'''
In a class room the teacher decides to shuffle all the students so that each student collaborates with other students too and she also checks that board is visible to all students. In a bench n number of students can be seated. She calls the students and makes them stand in a line.
She checks first two person and if the first person is taller than the second person he is put in second place and second in first, i.e., their positions are swapped. After swapping, the teacher checks second and third person height and if the second person is taller than third person their positions are swapped. She repeats this till the end. She finds that the last student is the tallest student after completing one iteration.
So she repeats the process for (n-1) times so that all students are sorted. She stops the process in the middle as soon as she find that the students are sorted.
For ex:
Consider 5 number of students can be seated in a bench
Their height order is in
6 4 3 2 5
During first comparison, adjacent numbers 6 and 4 is compared, 6 is greater than 4 hence the order becomes 4 6 3 2 5.
Again the teacher checks 6 and 3. 6 is greater than 3 hence the numbers are swapped and the order becomes 4 3 6 2 5.
She compares 6 and 2 and they get swapped and the order becomes 4 3 2 6 5. She compares 6 and 5 they get swapped and the order becomes 4 3 2 5 6.
She sees that they are not in order she again takes adjacent person heights and she swaps. She keeps doing this until the order becomes 2 3 4 5 6.
Help the teacher write a program to do bubble sorting inorder to sort the height in order.
For ex:
Consider 5 number of students can be seated in a bench
Their height is in order
6 4 3 2 5
During first comparison, adjacent numbers 6 and 4 is compared, 6 is greater than 4 hence the order becomes 4 6 3 2 5.
Again the teacher checks 6 and 3, 6 is greater than 3. Hence the numbers are swapped and the order becomes 4 3 6 2 5.
She compares 6 and 2 and they get swapped and the order becomes 4 3 2 6 5. She compares 6 and 5, they get swapped and the order becomes 4 3 2 5 6.
She sees that they are not in order. So she again compares adjacent person heights and she swaps. She repeats this until the heights get sorted. Finally the students will be seated in this order -  2 3 4 5 6.
 
Help the teacher write a program to do this task.

Input Format:Input consists of n+1 integers. The first integer corresponds to n, the number of elements in the array. The next n integers correspond to the elements in the array.

Output Format:Refer sample output for formatting specs.
'''
# Program:
my_list = []
swapped = True
num = int(input("Enter length of an array: "))

for i in range(num):
    val = int(input("Enter an element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("Sorted array: ",*my_list)

'''
Output:

Enter length of an array: 5
Enter an element: 6
Enter an element: 4
Enter an element: 3
Enter an element: 2
Enter an element: 5
Sorted array:  2 3 4 5 6
'''
