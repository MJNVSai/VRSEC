/* using difftime() function */
/* difftime(time_t time2,time_t time1) */
#include<stdio.h>
#include<conio.h>
#include<time.h>
int main()
{
    int i;
    time_t start,end;
    clrscr();
    start=time(NULL);
    for(i=1;i<=500;i++);
    getch();
    end=time(NULL);
    textcolor(5);
    cprintf("the diffrence of time from start to end = %f seconds",difftime(end,start));
getch();
return 0;
}

