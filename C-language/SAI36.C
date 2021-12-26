/* factorial of a number using while loop */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,i,fact=1;
clrscr();
printf("enter the decimal number= ");
scanf("%d",&n);
i=1;
while(i<=n){
fact*=i;
i++;
}
printf("factorial of %d is %d",n,fact);
getch();
}