t/* clear the bit */
#include<stdio.h>
#include<conio.h>
int main()
{
	int n1,n2;
	clrscr();
	printf("enter an integer= ");
	scanf("%d",&n1);
	printf("enter the bit position= ");
	scanf("%d",&n2);
	n1=n1 & (~(1 << n2));
	printf("result= %d",n1);
getch();
return 0;
}