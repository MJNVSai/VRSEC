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
public class Linear_Search 
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
        
        System.out.print("Enter Search Element : ");
        int k = sc.nextInt();
        int flag = 0;
        for(int i = 0; i < n; i++)
        {
            if(a[i] == k)
            {
                flag = 1;
                break;
            }
        }
        if(flag != 0)
        {
            System.out.println("Search Successfully");
        }
        else
        {
            System.out.println("Search UnSuccessfully");
        }
    }
}
