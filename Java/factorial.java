import java.io.*;
import java.util.*;

class factorial
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int n,fact = 1,i;

		System.out.println();
		System.out.println("Enter a number : ");
		n = s.nextInt();

		for(i = 1; i <= n; i++)
		{
			fact = fact*i;
		}

		System.out.println("Factorial of Given number : " + fact);
	}
}