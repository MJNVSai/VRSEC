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
public class Sum_of_rc 
{
    public static void main(String args[])
    {
        int i,j,rsum, csum = 0;
        int a[][] = new int[3][3];
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter Matrix 1 elements : ");
        for(i = 0; i < 3; i++)
        {
            for(j = 0; j < 3; j++)
            {
                a[i][j] = sc.nextInt();
            }
            System.out.println();
        }
        
        System.out.println("Sum of Each row : ");
        for(int k = 0; k < 3; k++)
        {
            rsum = 0;
            for(int l = 0; l < 3; l++)
            {
                rsum = rsum + a[k][l];
            }
            System.out.println("Row " + (k+1) + " sum : " + rsum);
        }
        
        System.out.println("Sum of Each Column : ");
        for(int k = 0; k < 3; k++)
        {
            csum = 0;
            for(int l = 0; l < 3; l++)
            {
                csum = csum + a[l][k];
            }
            System.out.println("Column " + (k+1) + " sum : " + csum);
        }
        
    }
}
