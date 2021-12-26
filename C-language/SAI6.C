/* division for limit of a decimal */
#include<stdio.h>
#include<conio.h>
int main()
{
float a,b,c;
clrscr();
printf("enter any two values= ");
scanf("%f %f",&a,&b);
c=a/b;
printf("%.3f",c);          /* here .3 decides the decimal upto 3 numbers */
getch();
}