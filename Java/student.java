import java.io.*;
import java.util.*;

class student
{
	public static void main(String args[])
	{
		Scanner s = new Scanner(System.in);
		int m1,m2,m3,average;
		double contact;
		String name,roll;
		char gender;

		System.out.println();
		System.out.println("Enter your Roll number : ");
		roll = s.next();

		System.out.println("Enter your Name : ");
		name = s.next();

		System.out.println("Enter your Gender : ");
		gender = s.next().charAt(0);

		System.out.println("Enter your Contact number : ");
		contact = s.nextDouble();
		System.out.println();

		System.out.println("Enter your Subject 1 marks : ");
		m1 = s.nextInt();

		System.out.println("Enter your Subject 2 marks : ");
		m2 = s.nextInt();

		System.out.println("Enter your Subject 3 marks : ");
		m3 = s.nextInt();
		System.out.println();

		average = (m1 + m2 + m3)/3;

		System.out.println("Total marks are : " + (m1 + m2 + m3));
		System.out.println("Average of marks are : " + (average));
	}
}