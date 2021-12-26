#include<stdio.h>
#include<conio.h>
int main()
{
int n,s;
clrscr();
printf("enter any one value= ");
scanf("%d %d",&n,&s);
if(n>s)
{
printf("given number is a big");
}
else
{
printf("given number is a small");
}
getch();
}