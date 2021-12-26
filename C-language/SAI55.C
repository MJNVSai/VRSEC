/* using clock() function */
/* clock_t clock(void) */
#include<stdio.h>
#include<conio.h>
#include<time.h>
void display()
{
	textcolor(9);
	cprintf("elapsed time was %u secs.\n",clock()/CLOCKS_PER_SEC);
}
int main()
{
	clrscr();
	getch();
	display();
	getch();
	display();
getch();
return 0;
}