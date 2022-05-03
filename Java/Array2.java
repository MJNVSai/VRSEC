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
public class Array2 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[10], e[] = new int[10], od[] = new int[10];
        System.out.println();
        
        System.out.println("Enter the Array elements : ");
        for(int i = 0; i < a.length; i++)
        {
            a[i] = sc.nextInt();
            if(i%2 == 0)
            {
                e[i] = a[i];
            }
            else
            {
                od[i] = a[i];
            }
        }
        System.out.print("Original Array elements are : ");
        for(int j = 0; j < a.length; j++)
        {
            System.out.print(a[j] + ", ");
        }
        System.out.println();
        
        System.out.print("Odd Array elements are : ");
        for(int j1 = 0; j1 < e.length; j1++)
        {
            System.out.print(e[j1] + ", ");
        }
        System.out.println();
        
        System.out.print("Even Array elements are : ");
        for(int j2 = 0; j2 < od.length; j2++)
        {
            System.out.print(od[j2] + ", ");
        }
    }
}
