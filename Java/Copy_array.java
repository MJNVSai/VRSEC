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
public class Copy_array 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int i,j;
        int a[] = new int[10],n;
        
        System.out.print("Enter array size : ");
        n = sc.nextInt();
        
        int b[] = new int[n];
        System.out.println("Enter Array elements : ");
        for(i = 0; i < n; i++)
        {
            a[i] = sc.nextInt();
        }
        for(j = 0; j < b.length; j++)
        {
            b[j] = a[j];
        }
        
        System.out.print("Original Array is : ");
        for(int l = 0; l < n; l++)
        {
            System.out.print(a[l] + " ");
        }
        System.out.println();
        System.out.print("Copied Array is : ");
        for(int k = 0; k < b.length; k++)
        {
            System.out.print(b[k] + " ");
        }
    }
}
