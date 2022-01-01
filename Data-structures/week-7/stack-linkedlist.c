/*
We have discussed linked list operations called insert() and delete() in the class.
Also illustrated with examples. Design and implement menu driven C program with 4 operations.
(1) Add element to list (2) Delete element from list (3) Traverse elements and (4) Exit.
Write all possible examples supported by relevant test cases.
*/

// Program:
// Stack using Linked List

#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;

}*tos,*new,*temp,*dis;

void push(int value)
{
    new = (struct node*)malloc(sizeof(struct node*));
    new->data = value;
    new->next = NULL;
    if(tos == NULL)
    {
        tos = new;
    }
    else
    {
        new->next = tos;
        tos = new;
    }
}

void pop()
{
    if(tos == NULL)
    {
        printf("stack is empty");
    }
    else
    {
        temp = tos; // copying the value;
        printf("deleted element: %d\n",tos->data);
        tos = tos->next; // to move the next value...
        temp->next = NULL;
        free(temp);
    }
}

void display()
{
    if(tos == NULL)
    {
        printf("Stack is Empty!");
    }
    else
    {
        dis = tos; // dis pointer is created to store the values of tos pointer..
        while(dis!=NULL)
        {
            printf("%d ",dis->data);
            dis = dis->next;
        }
        printf("\n");
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
Enter your choice: 1

enter your element to push: 55

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to push: 68

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 2
deleted element: 68

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 3
55 45 

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 4
*/
