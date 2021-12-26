/* l.c.m of two numbers */
#include<stdio.h>
#include<conio.h>
int main()
{
	int n1,n2,big;
	clrscr();
	printf("enter first integer= ");
	scanf("%d",&n1);
	printf("enter second integer= ");
	scanf("%d",&n2);
	big=(n1>n2)?n1:n2;
	while(1)
	{
	   if((big%n1==0)&&(big%n2==0))
	   {
		printf("L.C.M of %d and %d is %d",n1,n2,big);
		break;
	   }
	   big++;
	}
getch();
return 0;
}