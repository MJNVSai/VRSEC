/*
We have discussed Queue operations called insert() and delete() in the class.
Also illustrated with examples. Design and implement menu driven C program with 4 operations. 
(1) Add element to Queue (2) Delete element from Queue (3) Traverse elements and (4) Exit. 
Write all possible examples supported by relevant test cases. 
*/

// Program:

// Queue c program

#include<stdio.h>
#include<stdlib.h>
void insert(int);
int delete();
void traverse();
int front = 0,rear = 0,a[60] = {};

void insert(int y)
{
    int max_size = 6;
    if(rear >= max_size)
    {
        printf("Queue overflow");
    }
    else
    {
        rear++;
        a[rear] = y;
        
    }
}

int delete()
{
    int x;
    if((front == rear)||(rear == 0))
    {
        printf("Queue is empty");
    }
    else
    {
        front++;
        x = a[front];
        // printf("deleted element: %d\n",x);
        a[front] = '\0';
        // return x;
    }
}

void traverse()
{
    for(int i = 1;i <= 4;i++)
    {
        printf("%d\t",a[i]);
    }
}

int main()
{
    printf("=======================================\n\n");
    printf("-----------> MENU DRIVEN <-------------\n\n");
    printf("=======================================\n\n");
    while(1)
    {
        int z,a;
        printf("\nenter 1 ==> to insert\n");
        printf("enter 2 ==> to delete\n");
        printf("enter 3 ==> to traverse\n");
        printf("enter 4 ==> to exit\n");
        printf("\nEnter your choice: ");
        scanf("%d",&z);
        
        switch(z)
        {
            case 1:
                printf("enter your element to insert: ");
                scanf("%d",&a);
                insert(a);
                break;
            case 2:
                delete();
                break;
            case 3:
                traverse();
                break;
            case 4:
                exit(0);
        }
    }
    return 0;
}

// output: 
/*
=======================================

-----------> MENU DRIVEN <-------------

=======================================


enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to traverse
enter 4 ==> to exit

Enter your choice: 1
enter your element to insert: 45

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to traverse
enter 4 ==> to exit

Enter your choice: 1
enter your element to insert: 89

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to traverse
enter 4 ==> to exit

Enter your choice: 1
enter your element to insert: 13

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to traverse
enter 4 ==> to exit

Enter your choice: 2

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to traverse
enter 4 ==> to exit

Enter your choice: 3
0	89	13	0	
enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to traverse
enter 4 ==> to exit

Enter your choice: 4
*/
