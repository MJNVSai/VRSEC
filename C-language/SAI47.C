#include <stdio.h>
#include<conio.h>
#include <time.h>
#include<conio.h>
int main()
{
    struct tm* ptr;
    time_t lt;
    clrscr();
    lt = time(NULL);
    ptr = localtime(&lt);
    printf("%s\n", asctime(ptr));
    printf("current time -->%s\n",ctime(&lt));
    printf("current time --> %d:%d:%d\n",ptr->tm_hour,ptr->tm_min,ptr->tm_sec);
    printf("day of the month %d\n",ptr->tm_mday);
    printf("current month,year %d,%d\n",ptr->tm_mon,ptr->tm_year);
    printf("day of the week %d\n",ptr->tm_wday);
    printf("day in the year %d\n",ptr->tm_yday);
getch();
}