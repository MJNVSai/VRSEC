/*
We have discussed stack operations called push () and pop () in the class.
Also illustrated with examples. Design and implement menu driven C program with 4 operations.
(1) Add element to stack (2) Delete element from stack (3) Traverse elements and (4) Exit.
Write all possible examples supported by relevant test cases.(Use Dynamic Implementation for character data)
*/

// Program:
// Stack using Linked List with characters...

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;

}*tos,*new,*temp,*dis;

void push(char value)
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
        printf("deleted element: %c\n",tos->data);
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
        dis = tos;
        while(dis!=NULL)
        {
            printf("%c ",dis->data);
            dis = dis->next;
        }
        printf("\n");
    }
}

int main()
{
    while(1)
    {
        int z;
        char a[50];
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
                scanf("%s",a);
                int length = strlen(a);
                for(int i=0;i<length;i++)
                {
                    push(a[i]);
                }
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

enter your element to push: s

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to push: a

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to push: i

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to push: m

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 2
deleted element: m

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 3
i a s 

enter 1 ==> to push
enter 2 ==> to pop
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 4
*/
