/* delete the duplicate elements of an array */
#include<stdio.h>
#include<conio.h>
int main()
{
	int a[20],size,i,j,k;
	clrscr();
	printf("enter the no.of elements: ");
	scanf("%d",&size);
	printf("enter the array elements: ");
	for(i=0;i<size;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<size;i++)
	{
		for(j=i+1;j<size;j++)
		{
			if(a[i] == a[j])
			{
				for(k=j;k<size;k++)
				{
					a[k]=a[k+1];
				}
			   size--;
			   j--;
			}
		}
	}
	for(i=0;i<size;i++)
	{
		printf("%d\t",a[i]);
	}
getch();
return 0;
}