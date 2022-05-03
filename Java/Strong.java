/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pkg208w1a12a0;
import java.io.*;
import java.util.*;

/**
 *
 * @author SHREE
 */
public class Strong 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int n,sum = 0,fact,rem,temp,i;
        System.out.println();
        
        System.out.print("Enter a number : ");
        n = sc.nextInt();
        temp = n;
        
        while(n != 0)
        {
            rem = n%10;
            fact = 1;
            for(i = 1; i <= rem; i++)
            {
                fact = fact*i;
            }
            n = n/10;
            sum = sum + fact;
        }
        if(sum == temp)
        {
            System.out.println(sum + " is a Strong number");
        }
        else
        {
            System.out.println(sum + " is not an Strong number");
        }
    }
}
