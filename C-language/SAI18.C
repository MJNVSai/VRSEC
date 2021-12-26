/* to verify given number is prime or not */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,i,count=0;
clrscr();
printf("enter any one value= ");
scanf("%d",&n);
for(i=1;i<=n;i++){
if(n%i==0){
count++;
}
}
if(count>2){
printf("composite");
}
else{
printf("prime");
}
getch();
}