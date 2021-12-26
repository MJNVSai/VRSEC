/* using switch statement print add sub mul div square power of two numbers */
#include<stdio.h>
#include<conio.h>
#include<math.h>
int main()
{
int a,b,i;
clrscr();
printf("enter any two values= ");
scanf("%d %d",&a,&b);
printf("for add enter=1\nfor sub enter=2\nfor mul enter=3\nfor div enter=4\nfor square enter=5\nfor power enter=6\n");
scanf("%d",&i);
switch(i){
case 1:
printf("%d",a+b);
break;
case 2:
printf("%d",a-b);
break;
case 3:
printf("%d",a*b);
break;
case 4:
printf("%d",a/b);
break;
case 5:
printf("%d %d",a*a,b*b);
break;
case 6:
printf("%d",pow(a,b));
break;
}
getch();
}
