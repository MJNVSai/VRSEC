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
public class Desend_array 
{
    public static void main(String args[])
    {
        int a[] = new int[10];
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array Size: ");
        int n = sc.nextInt();
        System.out.println("Enter Array Elements : ");
        for(int i = 1; i < n+1; i++)
        {
            a[i] = sc.nextInt();
        }
        
        for(int i = 1; i <= n+1; i++)
        {
            for(int j = 1; j <= n-i; j++)
            {
                if(a[j] < a[j+1])
                {
                    int t = a[j+1];
                    a[j+1] = a[j];
                    a[j] = t;
                }
            }
        }
        System.out.print("Desending Order  Array : ");
        for(int i = 1; i <= n; i++)
        {
            System.out.print(a[i] + " ");
        }
    }
}
