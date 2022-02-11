/*
Reverse a linked list: Given pointer to the head node of a linked list, the task is to reverse the linked list. 
We need to reverse the list by changing the links between nodes.

Input: Head of following linked list 
1->2->3->4->NULL 
Output: Linked list should be changed to, 
4->3->2->1->NULL

*/

// Program:

#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;

}*new,*ptr,*prev,*curr,*temp;
struct node* head;

void push(int val){
    new = (struct node*)malloc(sizeof(struct node));
    new->data = val;
    new->next = NULL;
    
    if(head==NULL)
    {
        head = new;
    }
    else
    {
        ptr = head;
        while(ptr->next!=NULL)
        {
            ptr = ptr->next;
        }
        ptr->next = new;
    }
}
void reverse()
{
    ptr = head;
    prev = NULL;
    curr = head;
    while(curr!=NULL)
    {
        temp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = temp;
    }
    head = prev;
}
int main()
{
    push(10);
    push(20);
    push(30);
    push(40);
    push(50);
    
    ptr = head;
    reverse();
    ptr = head;
    printf("reverse of the Linked list: ");
    
    while(ptr!=NULL)
    {
        printf("%d ",ptr->data);
        ptr = ptr->next;
    }
    return 0;
}

/*
Output:

reverse of the Linked list: 50 40 30 20 10 

*/
