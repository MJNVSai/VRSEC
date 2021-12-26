/* maximum number in a array */
#include<stdio.h>
#include<conio.h>
int main()
{
int a[10],n,i,max=0;
clrscr();
printf("enter the size of an array= ");
scanf("%d",&n);
for(i=1;i<=n;i++){
scanf("%d",&a[i]);
}
for(i=1;i<=n;i++){
   if(max<a[i]){
   max=a[i];
   }
}
printf("maximum element :%d",max);
getch();
}
