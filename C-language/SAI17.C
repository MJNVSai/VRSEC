/* to verify given number is armstrong or not */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,num=0,rem,r;
clrscr();
printf("enter any one value= ");
scanf("%d",&n);
while(n!=0){
rem=n%10;
num=num+(rem*rem*rem);
n=n/10;
}
printf("%d",num);
r=num;
if(r==n){
printf("\ngiven number is an armstroing number");
}
else{
printf("\ngiven numbern is not a armstrong number");
}
getch();
}