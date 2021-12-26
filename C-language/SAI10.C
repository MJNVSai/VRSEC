#include<stdio.h>
#include<conio.h>
int main()
{
int n,i,fact=1;
clrscr();
printf("enter any one value= ");
scanf("%d",&n);
for(i=1;i<=n;i++){
fact=fact*i;
}
printf("%d",fact);
getch();
}

