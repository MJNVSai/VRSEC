/*
In a class room we have discussed the stack operations called push() and pop(). Based on these operations design and implement C/Python code to evaluate postfix expression. Hint: Use the following statement in the push function stack[top]=(int)(post[tmp]-48); for ASCII value conversion from string to numbers. For examples please refer http://www.btechsmartclass.com/data_structures/postfix-evaluation.html 
Sample Input-1:
Postfix Expression 5 3 + 8 2 - *
Sample Output-1: 
Postfix Expression Evaluation Value is 48
 Sample Input-2:
Postfix Expression 2 3 4 + * 6 -
Sample Output-2: 
Postfix Expression Evaluation Value is 8
*/

// Program:
#include<stdio.h>
#include<string.h>
int tos=-1,a[20];
void push(int p)
{
	int i;
    tos++;
    a[tos]=p;
}
int pop()
{
    int result;
    result=a[tos];
    tos--;
    return result;
}
int main()
{
    char str[20];
    int i,val1,val2,x;
    printf("\nEnter postfix expression:\n");
    gets(str);
    x=strlen(str);
    for(i=0;i<x;i++)
    {
        if(str[i]>=48 && str[i]<=57)
        {
            push(str[i]-48);
        }
        else
        {
            val1=pop();
            val2=pop();
            if(str[i]=='+')
            push(val1+val2);
            else if(str[i]=='-')
            push(val2-val1);
            else if(str[i]=='*')
            push(val1*val2);
            else if(str[i]=='/')
            push(val1/val2);
        }
    }
    printf("The result is:\n");
    printf("%d",a[tos]);
    return 0;
}

/*
Output:

Enter postfix expression:
234+*6-
The result is:
8
*/
