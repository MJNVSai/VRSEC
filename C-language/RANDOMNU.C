#include<stdio.h>
#include<conio.h>
#include<time.h>
void main()
{
	int number;
	clrscr();
	srand(time(NULL));
	number=rand()%50;
	/* the above line indicates that it generate a number between 0 to 50 only */
	printf("random number is %d\n",number);
getch();
}