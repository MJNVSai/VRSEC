/* reverse of a number */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,rev=0;
clrscr();
printf("enter any one value= ");
scanf("%d",&n);
while(n!=0){
rev=rev*10+n%10;
n=n/10;
}
printf("%d\t",rev);
getch();
}