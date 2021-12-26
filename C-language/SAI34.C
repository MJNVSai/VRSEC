/* to convert decimal number into binary */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,b[10],i,j;
clrscr();
printf("enter the binary number= ");
scanf("%d",&n);
i=0;
while(n>0){
b[i]=n%2;
n=n/2;
i++;
}
for(j=i-1;j>=0;j--){
printf("%d ",b[j]);
}
getch();
}