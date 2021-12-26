#include<stdio.h>
#include<conio.h>
#include<dos.h>
void main()
{
	int i;
	clrscr();
	for(i=0;i<10;i++){
	clrscr();
	textcolor(i+1);
	textbackground(i);
	cprintf("\n this is blader sai");
	sleep(1);
	}
getch();
}