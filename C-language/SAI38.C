/* to check strong number or not */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,temp,rem,sum,fact,i;
clrscr();
printf("enter the number= ");
scanf("%d",&n);
temp=n;
sum=0;
/* to find sum of factorial digits */
while(n>0){
	rem=n%10;
	/* FIND FACTORIAL OF REM */
	fact=1;
	for(i=1;i<=rem;i++){
	fact=fact*i;
	}
	/* add factorial to sum */
	sum=sum+fact;
	n=n/10;
	}
printf("sum :%d\n",sum);
printf("temp :%d\n",temp);
if(temp==sum){
  printf("%d is a strong number",temp);
  }
else{
  printf("%d is not a strong number",temp);
  }
getch();
}