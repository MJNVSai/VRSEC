/* change intensity of text in output */
#include<stdio.h>
#include<conio.h>
void main()
{
	clrscr();
	normvideo();
	textcolor(8);
	cprintf("\n normal quality text");
	getch();
	highvideo();
	textcolor(9);
	cprintf("\n high quality text");
	lowvideo();
	getch();
	textcolor(10);
	cprintf("\n low quality text");
	getch();
}