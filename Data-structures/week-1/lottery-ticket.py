'''
Rithick gets a lottery ticket and checks each number in the list to see whether he has won the lottery or not. Since there are many numbers,he finds it tedious to check each ticket number manually. So he decides to write a code to check whether he has won the lottery or not. Help Rithick write a code to find his lottery ticket number from the given ticket numbers.
Input Format:
First line of the input consists of n, that corresponds to total number of lottery tickets.
Next n lines consists of Integers, that corresponds to the given lottery ticket numbers.
Last line consists of an Integer 'l', which corresponds to Rithick's lottery ticket number.
Output Format:
Output consists of string "Congratulations! You have won the lottery" or "Sorry your ticket number is not there. Better luck next time", according to the search result.
Sample Input and Output:
[All text in bold corresponds to input and the rest corresponds to output]
Enter the total number of tickets:
5
Enter the ticket number 1:
4521
Enter the ticket number 2:
3589
Enter the ticket number 3:
147852
Enter the ticket number 4:
2365
Enter the ticket number 5:
8965
The ticket numbers are:
4521 3589 147852 2365 8965
Enter the ticket number to be searched:
8965
The ticket number 8965 is found at position 5
Congratulations!You have won the lottery
'''

# Program:
a = []
n = int(input("enter no of tickets: "))
found = 0
for i in range(1, n + 1):
    p = int(input(f"enter the ticket number{i}: "))
    a.append(p)
print("the ticket numbers are: \n", *a)

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

'''
Output:
enter no of tickets: 5
enter the ticket number1: 123
enter the ticket number2: 564
enter the ticket number3: 987
enter the ticket number4: 880
enter the ticket number5: 222
the ticket numbers are: 
 123 564 987 880 222
enter the ticket number to be search: 880
the ticket 880 is found at position:  3
congratulations you have won the lottery
end of the program
'''
