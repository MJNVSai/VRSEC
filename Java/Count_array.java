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
public class Count_array 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int i,j,n,count = 0;
        int a[] = new int[10];
        System.out.print("Enter Array Size : ");
        n = sc.nextInt();
        System.out.println("Enter Array elements : ");
        for(i = 0; i < n; i++)
        {
            a[i] = sc.nextInt();
        }
        System.out.print("Original Array : ");
        for(j = 0; j < n; j++)
        {
            System.out.print(a[j] + " ");
            count = count + 1;
        }
        System.out.println();
        System.out.print("NO.of elements in a Array : " + count);
    }
}
