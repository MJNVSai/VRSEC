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
public class Odd_Even 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int a[] = new int[10];
        int ev[] = new int[10];
        int od[] = new int[10];
        
        System.out.println("Enter Array Elements : ");
        for(int i = 0; i < a.length; i++)
        {
            a[i] = sc.nextInt();
            if(i%2 == 0)
            {
                ev[i] = a[i];
            }
            else
            {
                od[i] = a[i];
            }
        }
        System.out.println("Original Array Elements : ");
        for(int i = 0; i < a.length; i++)
        {
            System.out.print(a[i] + " ");
        }
        System.out.println();
        System.out.println("ODD Array Elements : ");
        for(int i = 0; i < ev.length; i++)
        {
            System.out.print(ev[i] + " ");
        }
        System.out.println();
        System.out.println("EVEN Array Elements : ");
        for(int i = 0; i < od.length; i++)
        {
            System.out.print(od[i] + " ");
        }
    }
}
