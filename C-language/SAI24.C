/* to find the ceil of the number */
#include<stdio.h>
#include<conio.h>
#include<math.h>
int main()
{
float a,s;                   /* ceil means higher roundoff of a number */
clrscr();
printf("enter any one value= ");
scanf("%f",&s);
a=ceil(s);
printf("result :%f",a);
getch();
}