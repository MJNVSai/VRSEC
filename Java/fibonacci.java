import java.io.*;
import java.util.*;

class fibonacci
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int a = 0,b = 1,c,i,n;

		System.out.println();
		System.out.println("Enter a number : ");
		n = s.nextInt();

		System.out.println("The fibonacci Series of first " + n + "numbers are : ");
		System.out.print(a + " " + b);

		for(i = 2; i < n; i++)
		{
			c = a + b;

			System.out.print(" " + c);
			a = b;
			b = c;
		}
		System.out.println();
	}
}