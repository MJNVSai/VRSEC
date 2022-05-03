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
public class Dupicate_array 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int i,j,n,count;
        int arr[] = new int[10];
        
        System.out.print("Enter array size : ");
        n = sc.nextInt();
        int dup[] = new int[n];
        
        System.out.println("Enter array Elements : ");
        for(i = 0; i < n; i++)
        {
            arr[i] = sc.nextInt();
        }
        
        System.out.print("Duplicate Elements are : ");
        for(j = 0; j < n; j++)
        {
            count = 0;
            for(int j1 = j + 1; j1 < n; j1++)
            {
                if(arr[j] == arr[j+1])
                {
                    count = count + 1;
                }
            }
            if(count > 1)
            {
                System.out.print(arr[j] + " ");
            }
        }
        
    }
}
