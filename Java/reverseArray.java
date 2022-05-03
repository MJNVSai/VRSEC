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
public class reverseArray 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int i,j,n;
        int a[] = new int[10];
        
        System.out.print("Enter Array size : ");
        n = sc.nextInt();
        
        System.out.println("Enter Array elements : ");
        for(i = 0; i < n; i++)
        {
            a[i] = sc.nextInt();
        }
        
        System.out.print("Original Array : ");
        for(int k = 0; k < n; k++)
        {
            System.out.print(a[k] + " ");
        }
        
        System.out.println();
        System.out.print("Reverse Array : ");
        for(j = n-1; j >= 0; j--)
        {
            System.out.print(a[j] + " ");
        }
    }
}
