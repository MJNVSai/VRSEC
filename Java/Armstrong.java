import java.io.*;
import java.util.*;

class Armstrong
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int n,temp,rem,add = 0;

		System.out.println();
		System.out.println("Enter a number : ");
		n = s.nextInt();
		temp = n;

		while(temp != 0)
		{
			rem = temp%10;
			add = add + (rem*rem*rem);
			temp = temp/10;
		}

		if(add == n)
		{
			System.out.println(n + " is an Armstrong number ");
		}
		else
		{
			System.out.println(n + " is not an Armstrong number ");
		}
	}
}