/* to find area and circumference of the circle */
#include<stdio.h>
#include<conio.h>
int main()
{
float r,a,c;
clrscr();
printf("enter the dimensions of the circle= ");
scanf("%f",&r);
a=3.14*r*r;
c=2*3.14*r;
printf("%.3f %.3f",a,c);
getch();
}