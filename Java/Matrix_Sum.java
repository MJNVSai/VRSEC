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
public class Matrix_Sum 
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int i,j,upper = 0,lower = 0,diag = 0;
        int a[][] = new int[3][3];
        
        System.out.println("Enter Matrix - 1 Elements : ");
        for(i = 0; i < 3; i++)
        {
            for(j = 0; j < 3; j++)
            {
                a[i][j] = sc.nextInt();
            }
            System.out.println();
        }
        
        for(int x = 0; x < 3; x++)
        {
            for(int y = 0; y < 3; y++)
            {
                if(x == y)
                {
                    diag = diag + a[x][y];
                }
                else if(x > y)
                {
                    upper = upper + a[x][y];
                }
                else if(x < y)
                {
                    lower = lower + a[x][y];
                }
            }
        }
        System.out.println("Sum of Diagonal Elements are : " + diag);
        System.out.println("Sum of Upper Bound Elements are : " + upper);
        System.out.println("Sum of Lower bound Elements are : " + lower);
    }
}
