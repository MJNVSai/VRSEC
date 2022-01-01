'''
In a class room we have discussed the stack operations called push() and pop().
Based on these operations design and implement the solution to identify the balanced and un-balanced expressions.
Sample Input-1
The expression like [(a+b)(a-b)] 
Sample output-1
is known to be balanced
Sample Input-2
The expression like [(a+b)(a-b] is known to be un-balanced
Sample output-2
is known to be un-balanced
Design algorithm and rules for the same. Use C/Python program for implementation.
'''
# Program:
open_list = ["[","{","("]
close_list = ["]","}",")"]

def parenthesis(myStr):
	stack = []
	for i in myStr:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return "Unbalanced"
	
	if len(stack) == 0:
		return "Balanced"
	else:
		return "Unbalanced"


string = input("enter the equation: ")
print(string,"- is a", parenthesis(string),"Equation")

'''
Output:

enter the equation: [(a+b)(a-b)]  
[(a+b)(a-b)] - is a Balanced Equation
'''
