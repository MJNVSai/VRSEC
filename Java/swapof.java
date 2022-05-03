import java.io.*;
import java.util.*;

class swapof
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int a,b,c;

		System.out.println();
		System.out.println("Enter any 2 numbers : ");
		a = s.nextInt();
		b = s.nextInt();
		System.out.println("Numbers after swapping are : " + a + " " + b);

		/* Swap logic */
		c = a;
		a = b;
		b = c;

		System.out.println("Numbers after swapping are : " + a + " " + b);
	}
}