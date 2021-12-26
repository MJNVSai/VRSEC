/* to check given number strong number or not */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,temp,i,sum=0,rem;
long fact=1;
clrscr();
printf("enter the number= ");
scanf("%d",&n);
temp=n;
while(n>0){                     /* the sum of factorials of a number
				is equal to the given number is called strong number */
rem=n%10;
for(i=1;i<=rem;i++){
fact=fact*i;
}
sum=sum+fact;
n/=10;
}
printf("temp %d\n",temp);
printf("sum :%d\n",sum);
if(sum==temp){
printf("%d is a strong number",temp);
}
else{
printf("%d is not a strong number",temp);
}
getch();
}