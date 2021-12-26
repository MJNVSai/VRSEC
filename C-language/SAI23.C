/* to find square root a number */
#include<stdio.h>
#include<conio.h>
#include<math.h>
int main()
{                             /* we can write it as b=sqrt(x) and print b we get the same result */
float x;
clrscr();
printf("enter the value= ");
scanf("%f",&x);
printf("result :%.3f",sqrt(x));
getch();
}