/* to print greatest & smallest using ternary operator */
#include<stdio.h>
#include<conio.h>
int main()
{
int a,b,c,big,small;
clrscr();
printf("enter any three numbers= ");
scanf("%d %d %d",&a,&b,&c);
big=(a>b&&a>c)?(a):((b>c)?(b):(c));
small=(a<b&&a<c)?(a):((b<c)?(b):(c));
printf("greatest number :%d\n",big);
printf("smallest number :%d\n",small);
getch();
}