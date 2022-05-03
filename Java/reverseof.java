import java.io.*;
import java.util.*;

class reverseof
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int n,rev = 0,r;

		System.out.println();
		System.out.println("Enter a number : ");
		n = s.nextInt();

		while(n > 0)
		{
			r = n%10;
			rev = (rev*10) + r;
			n = n/10;
		}
		System.out.println("Reverse of the number : " + rev);
	}
}