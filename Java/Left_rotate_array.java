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
public class Left_rotate_array 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int i,j,p = 2,x,n;
        int a[] = new int[10];
        
        System.out.print("Enter Array length : ");
        n = sc.nextInt();
        System.out.println("Enter Array elements : ");
        for(i = 0; i < n; i++)
        {
            a[i] = sc.nextInt();
        }
        
        for(j = 1; j <= p; j++)
        {
            x = a[0];
            for(int k = 0; k < n-1; k++)
            {
                a[k] = a[k+1];
            }
            a[n-1] = x;
        }
        
        System.out.print("Left Rotated array : ");
        for(int l = 0; l < n; l++)
        {
            System.out.print(a[l] + " ");
        }
    }
}
