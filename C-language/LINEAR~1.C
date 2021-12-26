#include<stdio.h>
#include<conio.h>

int main()
{
    int array[100],search,c,n;
    clrscr();

    printf("enter the length of the array: ");
    scanf("%d",&n);
    printf("enter %d integers: \n",n);

    for(c=0;c<n;c++)
    {
	scanf("%d",&array[c]);
    }

    printf("enter a number to search: ");
    scanf("%d",&search);

    for(c=0;c<n;c++)
    {
	if(array[c]==search)
	{
	    printf("%d is present at location %d.\n",search,c+1);
	    break;
	}
    }

    if(c==0)
    {
	printf("%d isn't present in the array.\n",search);
    }

    getch();
    return 0;
}