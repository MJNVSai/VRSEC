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
public class Perfect 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println();
        
        int num,rem,sum = 0,temp,i;
        System.out.print("Enter a Number : ");
        num = sc.nextInt();
        temp = num;
        
        for(i = 1; i < num; i++)
        {
            rem = num%i;
            if(rem == 0)
            {
                sum = sum + i;
            }
        }
        if(sum == temp)
        {
            System.out.println(sum + " is an Perfect number");
        }
        else
        {
            System.out.println(sum + " is not a Perfect number");
        }
    }
}
