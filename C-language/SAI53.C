/* lcm of continous numbers and their sum */
#include<stdio.h>
#include<conio.h>
int lcm(int,int);
int main()
{
	int n,i,l=0;
	clrscr();
	printf("enter the first integer= ");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		l=l+lcm(i,n);   /* or yu can take lcm=lcm+LCM(i,n); */
	}
	textcolor(5);
	cprintf("sum of lcm's is = %d",l);
getch();
return 0;
}
int lcm(int x,int y)
{
	int big;
	big=(x>y) ? x:y;
	while(1)
	{
		if((big%x==0)&&(big%y==0))
		{
			break;
		}
		big++;
	}
return big;
}
