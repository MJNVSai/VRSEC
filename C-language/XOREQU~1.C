/* XOR EQUALITY */
#include<stdio.h>
#include<math.h>
#include<conio.h>
int main()
{
	int t,n,i;
	long long int m,x,a=0;
	clrscr();
	if(1<=t<=pow(10,5))
	{
		printf("enter no.of test cases= ");
		scanf("%d",&t);
	}
	while(t--)
	{
		printf("enter an integer= "); 
		scanf("%d",&n);
		if(1<=n<=pow(10,5))
		{
			for(i=0;i<(pow(2,n)-1);i++) 
			{
				x=i;
				if(x%2==0)
				{
				   x^(x+1) == (x+2)^(x+3);
				   a++;
				}
			}
		printf("%lld\n",a);
		m=(pow(10,9)+7);
		printf("%lld\n",m);
		printf("result=  %lld\n",(a%m));
		a=0;
		}
	}
getch();
return 0;
}