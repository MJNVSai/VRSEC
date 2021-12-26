/* ELECTRICITY BILL PROGRAM */
#include<stdio.h>
#include<conio.h>
int main()
{
float x;
clrscr();
printf("enter no.of units consumed= ");
scanf("%f",&x);
if(x<=199){
printf("electricity bill :%f",x*(1.20));
}
else if((x>=200)&&(x<=400)){
printf("electricity bill :%f",x*(1.50));
}
else if((x>=400)&&(x<=600)){
printf("electricity bill :%f",x*(1.80));
}
else{
printf("electricity bill :%f",x*(2.00));
}
getch();
}