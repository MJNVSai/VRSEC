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
public class Reverse_Array 
{
    public static void main(String args[])
    {
        int i,j;
        int a[][] = new int[2][2];
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter array elements : ");
        for(i = 0; i < 2; i++)
        {
            for(j = 0; j < 2; j++)
            {
                a[i][j] = sc.nextInt();
            } 
        }
        
        System.out.println("Reverse Matrix : ");
        for(int k = 1; k >= 0; k--)
        {
            for(int l = 1; l >= 0; l--)
            {
                System.out.print(a[k][l] + " ");
            }
            System.out.println();
        }
    }
}
