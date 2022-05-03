import java.io.*;
import java.util.*;

class Palindrome
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int n,temp,rem,rev = 0;

		System.out.println();
		System.out.println("Enter a number : ");
		n = s.nextInt();
		temp = n;

		while(temp > 0)
		{
			rem = temp%10;
			rev = (rev*10) + rem;
			temp = temp/10;
		}

		if(rev == n)
		{
			System.out.println(n + " is an Palindrome number ");
		}
		else
		{
			System.out.println(n + " is not an Palindrome number ");
		}
	}
}