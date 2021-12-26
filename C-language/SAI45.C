#include<stdio.h>
#include<dos.h>
#include<conio.h>
void main()
{
	clrscr();
	textbackground(4);
	textcolor(5);
	for(;!kbhit();)   // kbhit=keyboard hit
	{
	   printf("\n press any key to stop me........\n");
	   delay(800);//delay in milli seconds
	 }
getch();
}
