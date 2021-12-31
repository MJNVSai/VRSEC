/*
We have discussed stack operations called push () and pop () in the class. 
Also illustrated with examples. 
Design and implement menu driven C program with 4 operations. 
(1) Add element to stack (2) Delete element from stack (3) Traverse elements and (4) Exit. 
Write all possible examples supported by relevant test cases.
*/

// Program:
#include<stdio.h>
#include<stdlib.h>
void push(int);
int pop();
void display();
int tos = -1,a[5] = {};

void push(int y)
{
    int max_size = 5;
    if(tos >= max_size)
    {
        printf("stack overflow");
    }
    else
    {
        tos++;
        a[tos] = y;
        
    }
}

int pop()
{
    int x;
    if(tos <= 0)
    {
        printf("stack is empty");
    }
    else
    {
        x = a[tos];
        tos--;
        return x;
    }
}

void display()
{
    for(int i = 1;i <= 4;i++)
    {
        printf("%d\t",a[i]);
    }
}

int main()
{
    while(1)
    {
        int z,a;
        printf("\nenter 1 ==> to push");
        printf("\nenter 2 ==> to pop");
        printf("\nenter 3 ==> to display");
        printf("\nenter 4 ==> to exit");
        printf("\nEnter your choice: ");
        scanf("%d",&z);
        switch(z)
        {
            case 1:
                printf("\nenter your element to push: ");
                scanf("%d",&a);
                push(a);
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
        }
    }
    return 0;
}

/*
Output:


enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to push: 45

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 2 1

enter your element to push: 70

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 2

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 3
70	0	0	0	
enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 4
*/
