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
public class Bignum 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println();
        
        int max,min,n,temp,rem;
        System.out.print("Enter a number : ");
        n = sc.nextInt();
        temp = n;
        
        max = n%10;
        min = n%10;
        while(n != 0)
        {
            rem = n%10;
            if(rem > max)
            {
                max = rem;
            }
            if(rem < min)
            {
                min = rem;
            }
            n = n/10;
        }
        System.out.println("Result : " + max + " " + min);
    }
}
