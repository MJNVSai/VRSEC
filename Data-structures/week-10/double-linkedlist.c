/*
Design and Implement a program to create double linked list. Use the following pseudocode.
Justify your solution with all the possible test cases. 

// Pseudocode:
// create node
1.	Struct node
2.	{
3.	Struct node *prev;
4.	Int data;
5.	Struct nodel * next;
6.	} *new,*temp,*head;
// create double linked list
1.	do
2.	{
3.	….
4.	….
5.	….
6.	….
7.	….
8.	….
9.	If(head=NULL) 
10.	{
11.	Head=new;
12.	Temp=new;
13.	}
14.	else
15.	{
16.	….
17.	….
18.	….
19.	}
20.	Printf(“do you need one more term”);
21.	Scanf(“%c”,&ch);
22.	}while(ch==’y’);

*/

// Program:

#include <stdio.h>
#include <stdlib.h>
 
int flag,e;
 
struct node
{
    struct node*prev;
    int data;
    struct node*next;
}*new,*head,*temp,*helper;
 
// double linked list
 
void dll()
{

    do
    {
    printf("Enter an element : ");
    scanf("%d",&e);
    new = (struct node*)malloc(sizeof(struct node*));
    new->prev = NULL;
    new->data = e;
    new->next = NULL;
    
    if(head == NULL)
    {
        head = new;
        temp = new;
    }
    else
    {
        new->prev = head;
        head->next = new;
        head = head->next;
    }
    printf("Do you want to enter an other node (1/0) : ");
    scanf("%d",&flag);
    
    }while(flag==1);
}

void display()
{
    helper = temp;
    printf("NULL ");
    while(helper!=NULL)
    {
        printf("%d ",helper->data);
        helper = helper->next;
    }
    printf("NULL");
}
 
int main()
{
    dll();
    display();
 
    return 0;
}

/*
OUTPUT:

Enter an element : 10
Do you want to enter an other node (1/0) : 1
Enter an element : 20
Do you want to enter an other node (1/0) : 1
Enter an element : 30
Do you want to enter an other node (1/0) : 1
Enter an element : 40
Do you want to enter an other node (1/0) : 1
Enter an element : 50
Do you want to enter an other node (1/0) : 0
NULL 10 20 30 40 50 NULL

*/
