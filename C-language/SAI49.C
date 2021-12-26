/* set the bit value */
#include<stdio.h>
#include<conio.h>
int main()
{
	int n,s;
	clrscr();
	printf("enter any one value= ");
	scanf("%d",&n);
	printf("enter the bit position=  ");
	scanf("%d",&s);
	n=n|(1<<s);
	printf("result= %d",n);
getch();
return 0;
}
