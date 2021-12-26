/* to find the power the value */
#include<stdio.h>
#include<conio.h>
#include<math.h>
int main()                     /* pow=power,pow(base,power) like pow(2,3)=8 */
{
int x,y;
clrscr();
printf("enter any two values= ");
scanf("%d %d",&x,&y);
printf("result :%f",pow(x,y));
getch();
}