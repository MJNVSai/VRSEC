import java.io.*;
import java.util.*;


class Mean
{
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int count = 0, sum = 0, n;
		double  mean;

		System.out.println();
		System.out.println("Enter the Sequence of numbers : ");

		while(sc.hasNextInt())
		{
			n = sc.nextInt();
			sum = sum + n;
			count = count + 1;
		}
		mean = sum/count;
		System.out.println("Mean of Numbers : " + mean);
	}
}