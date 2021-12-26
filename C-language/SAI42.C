/* colour ful c-program using gotoxy */
#include<stdio.h>
#include<conio.h>
void main()
{
	int x=0;
	clrscr();
	textbackground(8);
	gotoxy(15,10);
	textcolor(10);
	cprintf("enter any one number= ");
	textcolor(4);
	cscanf("%d",&x);
	textbackground(1);
	gotoxy(15,12);
	textcolor(9);
	cprintf("the number is: %d",x);
getch();
getch();
}
