#include<stdio.h>
#include<conio.h>
int main()
{
int a,b,c=0,i;
clrscr();
printf("enter any two values= ");
scanf("%d %d",&a,&b);
for(i=0;i<a;i++)
{
c=c+i;
if(c>2)
{
printf("%d",c);
break;
}
}
getch();
}
