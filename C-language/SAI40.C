/* generating the random number from one limit to another limit */
#include<stdio.h>
#include<conio.h>
#include<time.h>
int main()
{
	int number,lower,upper;
	clrscr();
	printf("enter the lower limit=\t");
	scanf("%d",&lower);
	printf("enter the upper limit=\t");
	scanf("%d",&upper);
	srand(time(NULL));
	number=rand()%((upper+lower)+1);
	printf("the random number from %d to %d is %d\n",lower,upper,number);
	printf("the random number from %d to %d is %d\n",lower,upper,number);
getch();
return 0;
}