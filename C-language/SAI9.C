#include<stdio.h>
#include<conio.h>
int main()
{
int a,b;
clrscr();
printf("enter any two values= ");
scanf("%d %d",&a,&b);
a=a+b;
b=a-b;
a=a-b;
printf("%d %d",a,b);
getch();
}