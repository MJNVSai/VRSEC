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
public class Frequency_array 
{
   public static void main(String args[])
   {
       Scanner sc = new Scanner(System.in);
       int i,j,n,visit = -1,count;
       int arr[] = new int[10];
       
       System.out.print("Enter array size : ");
       n = sc.nextInt();
       int freq[] = new int[n];
       
       System.out.println("Enter array Elements : ");
       for(i = 0; i < n; i++)
       {
           arr[i] = sc.nextInt();
       }
       
       for(j = 0; j < n; j++)
       {
           count = 0;
           for(int k = j+1; k < n; k++)
           {
               if(arr[j] == arr[k])
               {
                   count = count + 1;
                   freq[k] = visit;
               }
           }
           if(freq[j] != visit)
           {
               freq[j] = count + 1;
           }
       }
       
       System.out.print("The Original Array : ");
       for(int j2 = 0; j2 < n; j2++)
       {
           System.out.print(arr[j2] + " ");
       }
       System.out.println();
       System.out.print("Frequency of the Original Array : ");
       for(int j1 = 0; j1 < n; j1++)
       {
           if(freq[j1] != visit)
           {
               System.out.print(freq[j1] + " ");
           }
       }
   }
}
