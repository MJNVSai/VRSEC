/*
We have discussed queue operations called insert () and delete () in the class.
Also illustrated with examples. Design and implement menu driven C program with 4 operations.
(1) Add element to Queue (2) Delete element from Queue (3) Traverse elements and (4) Exit.
Write all possible examples supported by relevant test cases.(Use Dynamic Implementation for character data)
*/

// program:
// Queue using linked-list with characters.
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct node
{
    int data;
    struct node *next;
}*new,*front,*rear,*temp;

void insert(char value)
{
    new = (struct node*)malloc(sizeof(struct node*));
    new->data = value;
    new->next = NULL;
    
    if(rear == NULL && front == NULL)
    {
        front = new;
        rear = new;
    }
    else
    {
        rear->next = new;
        rear = new;
    }
}

void delete()
{
    if(front == NULL && rear == NULL)
    {
        printf("Queue is empty");
    }
    else
    {
        temp = front;
        printf("Deleted element: %c\n",front->data);
        front = front->next;
        temp->next = NULL;
        free(temp);
    }
}

void display()
{
    if(front == NULL && rear == NULL)
    {
        printf("Queue is empty");
    }
    else
    {
        while(front!=NULL)
        {
            printf("%c ",front->data);
            front = front->next;
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
        printf("\nenter 1 ==> to insert");
        printf("\nenter 2 ==> to delete");
        printf("\nenter 3 ==> to display");
        printf("\nenter 4 ==> to exit");
        printf("\nEnter your choice: ");
        scanf("%d",&z);
        switch(z)
        {
            case 1:
                printf("\nenter your element to insert: ");
                scanf("%s",a);
                
                int length = strlen(a);
                for(int i = 0; i < length; i++)
                {
                    insert(a[i]);
                }
                break;
            case 2:
                delete();
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


enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to insert: m

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to insert: s

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to insert: a

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 1

enter your element to insert: i

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 2
Deleted element: m

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 3
s a i 

enter 1 ==> to insert
enter 2 ==> to delete
enter 3 ==> to display
enter 4 ==> to exit
Enter your choice: 4
*/
