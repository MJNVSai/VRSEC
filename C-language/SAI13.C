#include<stdio.h>
#include<conio.h>
int main()
{
int a;
clrscr();
printf("enter any one value= ");
scanf("%d",&a);
while(a>=0){
printf("%d\t",a);
a--;
if(a==0){
break;
}
}
getch();
}
