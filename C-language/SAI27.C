/* to print an array dynamically */
#include<stdio.h>
#include<conio.h>
int main()
{
int a[30],i,n;
clrscr();
printf("enter the length of an array= ");
scanf("%d",&n);
for(i=0;i<=n;i++){
scanf("%d",&a[i]);
}
printf("\nresultant array : ");
for(i=0;i<=n;i++){
printf("%d ",a[i]);
}
getch();
}
