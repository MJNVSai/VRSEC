#include<stdio.h>
#include<conio.h>
int main()
{
     FILE *fp1,*fp2,*fp3;
     char ch;
     char fname1[95],fname2[98],fname3[100];
     clrscr();
     printf("enter the name of first file: ");
     scanf("%s",fname1);
     printf("enter the name of second file: ");
     scanf("%s",fname2);
     printf("enter the name of third file: ");
     scanf("%s",fname3);
     fp1=fopen(fname1,"r");
     fp2=fopen(fname2,"r");
     fp3=fopen(fname3,"w");
     if(fp1==NULL||fp2==NULL||fp3==NULL)
     {
       printf("\nfiles can't be opened\n");
       exit(EXIT_FAILURE);
     }
     while((ch=fgetc(fp1))!=EOF)
     {
	fputc(ch,fp3);
     }
     while((ch=fgetc(fp2))!=EOF)
     {
	fputc(ch,fp3);
     }
     printf("\n merged files fp1,fp2 into fp3 \n");
     fclose(fp1);
     fclose(fp2);
     fclose(fp3);
getch();
}

