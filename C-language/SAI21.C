/* to print square star pattern */
#include<stdio.h>
#include<conio.h>
int main()
{
int n,i,j;
clrscr();
printf("enter the no.of rows= ");
scanf("%d",&n);
for(i=1;i<n;i++){
for(j=1;j<n;j++){
printf("*\t");
}
printf("\n");
}
getch();
}