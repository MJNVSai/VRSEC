/* using of mktime() function */
// mktime() means making of your own time */
#include<stdio.h>
#include<conio.h>
#include<time.h>
int main()
{
	struct tm t;
	time_t timeinc;    /* c means calender */
	clrscr();
	t.tm_year= 2021-1900;
	t.tm_mon=  4;
	t.tm_mday= 6;
	t.tm_hour= 0;
	t.tm_min=  0;
	t.tm_sec=  0;
	t.tm_isdst= 0;
	timeinc = mktime(&t);
	printf(ctime(&timeinc));
getch();
return 0;
}