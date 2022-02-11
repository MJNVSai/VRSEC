/*
A polynomial p(x) is the expression in variable x which is in the form (axn + bxn-1 + …. + jx+ k), where a, b, c …., k fall in the category of real numbers and 'n' is non negative integer.
which is called the degree of polynomial. Create a function that takes two sorted linked lists and merges them into a single sorted linked list. Your goal is to return a new linked list that contains the nodes from two lists in sorted order.
You may assume the sort order is ascending.

For example:
// list1
1 -> 4 -> 10 -> 11

// list2
-1 -> 2 -> 3 -> 6

// merged list
-1 -> 1 -> 2 -> 3 -> 4 -> 6 -> 10 -> 11

*/

// Program:

#include<stdio.h>
#include<stdlib.h>

struct node
{
    int val;
    struct node* next;
}*head1,*head2,*new,*ptr;

void push(struct node** head,int val)
{
    new = (struct node*)malloc(sizeof(struct node));
    new->val = val;
    new->next = NULL;
    
    if(*head==NULL)
    {
        *head = new;
    }
    else
    {
        ptr = *head;
        while(ptr->next!=NULL)
        {
            ptr = ptr->next;
        }
        ptr->next = new;
    }
}
struct node* solution(struct node* res)
{
    struct node* ptr = res;
    while(head2&&head1)
    {
        res->next = (struct node*)malloc(sizeof(struct node));
        if(head1->val<head2->val)
        {
            res->next->val = head1->val;
            head1 = head1->next;
        }
        else
        {
            res->next->val = head2->val;
            head2 = head2->next;
        }
        res->next->next = NULL;
        res = res->next;
    }
    if(head2!=NULL)
    {
        while(head2)
        {
            res->next = (struct node*)malloc(sizeof(struct node));
            res->next->val = head2->val;
            res->next->next = NULL;
            res = res->next;
            head2 = head2->next;
        }
    }
    else
    {
        while(head1)
        {
            res->next = (struct node*)malloc(sizeof(struct node));
            res->next->val = head1->val;
            res->next->next = NULL;
            res = res->next;
            head1 = head1->next;
        }
    }
    return ptr->next;
    
}
int main()
{
    struct node* res;
    res = (struct node*)malloc(sizeof(struct node));
    
    push(&head1,1);
    push(&head1,4);
    push(&head1,10);
    push(&head1,11);
    
    push(&head2,1);
    push(&head2,2);
    push(&head2,3);
    push(&head2,6);
    
    ptr = solution(res);
    while(ptr!=NULL)
    {
        printf("->%d",ptr->val);
        ptr = ptr->next;
    }
}

/*

Output:

->1->1->2->3->4->6->10->11

*/
