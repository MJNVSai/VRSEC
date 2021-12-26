/* c program greatest among 3 numbers */
#include<stdio.h>
#include<conio.h>
int main()
{
int a,b,c;
clrscr();
printf("enter any three numbers= ");
scanf("%d %d %d",&a,&b,&c);
if(a>b&&a>c){
printf("a is greatest");
}
else if(b>c&&b>a){
printf("b is greatest");
}
else if(c>a&&c>b){
printf("c is greatest");
}
else{
printf("nothing is greatest");
}
getch();
}