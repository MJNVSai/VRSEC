/* to find the floor of the given number */
#include<stdio.h>
#include<conio.h>
#include<math.h>
int main()
{                            /* floor=lower round off value */
float x,b;
clrscr();
printf("enter any one value=  ");
scanf("%f",&x);
b=floor(x);                   /* we can write it as in printf floor(x) */
printf("result :%f",b);
getch();
}