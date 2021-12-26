/* adding of numbers using command line arguments */
#include<stdio.h>
#include<conio.h>
#include<dos.h>
int main(int argc,char *argv[])
{
clrscr();
  if(argc>2)
  {
    char *s1=argv[1];
    int x=atio(s1);
    char *s2=argv[2];
    int y=atio(s2);
    printf("sum is %d",x+y);
  }
  else{
    printf("in sufficient inputs");
  }
  return 0;
  }