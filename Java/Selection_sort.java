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
public class Selection_sort 
{
    public static void main(String args[])
    {
        int a[] = new int[10];
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter array Size: ");
        int n = sc.nextInt();
        System.out.println("Enter Array Elements : ");
        for(int i = 0; i < n; i++)
        {
            a[i] = sc.nextInt();
        }
        for(int i = 0; i < n; i++)
        {
            for(int j = i+1; j < n; j++)
            {
                if(a[i] > a[j])
                {
                    int t = a[i];
                    a[i] = a[j];
                    a[j] = t;
                }
            }
        }
        System.out.print("Sorted Array : ");
        for(int i = 0; i < n; i++)
        {
            System.out.print(a[i] + " ");
        }
    }
}
