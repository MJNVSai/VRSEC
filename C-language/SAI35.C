/* reverse of a number */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,rem,rev=0;
clrscr();
printf("enter a number to be reversed= ");
scanf("%d",&n);
while(n!=0){
rem=n%10;
rev=(rev*10)+rem;
n=n/10;
}
printf("reversed number is %d",rev);
getch();
}