/* to calculate area and perimeter of the rectangle */
#include<stdio.h>
#include<conio.h>
int main()
{
int a,p,l,b;
clrscr();
printf("enter the dimensions of the rectangle= ");
scanf("%d %d",&l,&b);
a=l*b;
p=2*(l+b);
printf("dimensions of rectangle are :%d %d",a,p);
getch();
}