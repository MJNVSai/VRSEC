/* sum  of first and last digit of a number */
#include<stdio.h>
#include<conio.h>
int main()
{
	int n, first, last;
	clrscr();
	printf("enter an integer value: ");
	scanf("%d",&n);
	last = n%10;
	while(n!=0)
	{
		first = n;
		n = n/10;
	}
	printf("sum of first and last digit of a number: %d",first+last);
getch();
return 0;
}
