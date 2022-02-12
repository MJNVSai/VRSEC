/*
In a class room we have discussed the algorithms for different traversal techniques like
(i) Inorder (ii) preorder and (iii) postorder. Based on the same discussion implement a solution.
Use the following LOC and complete the implimenation part.
Also run all the possible testcases. 

1.	struct node
2.	{
3.	int num;
4.	struct node *left;
5.	struct node *right;
6.	};
7.	void main()
8.	{
9.	struct node *v1,*v2,*v3,*v4,*v5,*v6,*v7;
10.	v1=create();
11.	v2=create();
12.	-----------------
13.	-----------------
14.	-----------------
15.	-----------------
16.	-----------------
17.	v1->left=v2;
18.	v1->right=v3;
19.	v2->left=v4;
20.	v2->right=v5;
21.	v3->left=v6;
22.	v3->right=v7;
23.	printf("\nInorder:");
24.	inorder(v1);
25.	printf("\nPreorder:");
26.	preorder(v1);
27.	printf("\nPostorder:");
28.	postorder(v1);
29.	getch();
30.	}
31.	struct node *create()
32.	{
33.	struct node *temp;
34.	temp=(struct node *)malloc(sizeof(struct node));
35.	temp->left=NULL;
36.	temp->right=NULL;
37.	printf("Enter value:");
38.	scanf("%d",&temp->num);
39.	return temp;
40.	}
41.	void inorder(struct node *T)
42.	{
43.	if(T!=NULL)
44.	{
45.	inorder(T->left);
46.	
47.	inorder(T->right);
48.	}
49.	}
50.	void preorder(struct node *T)
51.	{
52.	
53.	
54.	
55.	
56.	
57.	}
58.	}
59.	void postorder(struct node *T)
60.	{
61.	if(T!=NULL)
62.	{
63.	postorder(T->left);
64.	postorder(T->right);
65.	printf("%d",T->num);
66.	}
67.	}

*/

// Program:

#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data; // like root
    struct node *left;
    struct node *right;
};


struct node *create()
{
    struct node *temp;
    temp=(struct node *)malloc(sizeof(struct node));
    temp->left=NULL;
    temp->right=NULL;
    printf("Enter a node value : ");
    scanf("%d",&temp->data);
    return temp;
}


void inorder(struct node *T)
{
    if(T!=NULL)
    {
        inorder(T->left);
        printf("%d ",T->data);
        inorder(T->right);
    }
}


void preorder(struct node *T)
{
    if(T!=NULL)
    {
        printf("%d ",T->data);
        preorder(T->left);
        preorder(T->right);
    }	
}

void postorder(struct node *T)
{
    if(T!=NULL)
    {
        postorder(T->left);
        postorder(T->right);
        printf("%d ",T->data);
    }
}

void main()
{
    struct node *v1,*v2,*v3,*v4,*v5,*v6,*v7;
    v1=create();
    v2=create();
    v3=create();
    v4=create();
    v5=create();
    v6=create();
    v7=create();

    v1->left = v2;
    v1->right= v3;
    v2->left = v4;
    v2->right= v5;
    v3->left = v6;
    v3->right= v7;
    
    printf("\nInorder : ");
    inorder(v1);
    printf("\n\n");
    printf("\nPreorder : ");
    preorder(v1);
    printf("\n\n");
    printf("\nPostorder : ");
    postorder(v1);

}

/*
OUTPUT:

Enter a node value : 1
Enter a node value : 2
Enter a node value : 6
Enter a node value : 4
Enter a node value : 7
Enter a node value : 8
Enter a node value : 9

Inorder : 4 2 7 1 8 6 9 


Preorder : 1 2 4 7 6 8 9 


Postorder : 4 7 2 8 9 6 1 

*/
