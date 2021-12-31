/*
You have an empty sequence, and you will be given 
queries. Each query is one of these three types:
1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Function Description 
Complete the getMax function in the editor below. 
getMax has the following parameters: 
- string operations[n]: operations as strings 
Returns 
- int[]: the answers to each type 3 query 
Input Format
The first line of input contains an integer,  The next lines each contain an above mentioned query. 
Constraints 

All queries are valid. 
Sample Input
STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3
Sample Output
26
91
*/

// Program:
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int tos = 0;
char arr[50] ;

void push(char x){
    if (tos>20){
        printf("Stack Overflow");
    }
    else{
        tos++;
        arr[tos] = x;
    }
}

int pop(){
    if(tos<=0){
        printf("Stack empty");
    }
    else{
        char y = arr[tos];
        tos--;
        return y;
    }
}

int getMax()
{
    int i,max;
    max = arr[0];
    if(tos!=0)
    {
        for(i=1;i<=tos;i++)
        {
            if(max<arr[i])
            {
                max = arr[i];
            }
        }
        // printf("maximum element: %d\n",max);
    }
    else
    {
        printf("stack is empty");
    }
    return max;
}

int main()
{
 int k,h,j,d;
 printf("enter no.of inputs: ");
 scanf("%d",&h);
 
 for(j = 1; j <= h; j++)
 {
     printf("enter element: ");
     scanf("%d",&k);
     push(k);
 }
 
 pop();
 
 d = getMax();
 printf("maximum element: %d",d);
 
 return 0;
 
}

/*
Output:

enter no.of inputs: 3
enter element: 10
enter element: 5
enter element: 20
maximum element: 10
*/
