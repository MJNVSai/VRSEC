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
public class Matrix_transpose 
{
    public static void main(String args[])
    {
        int i,j;
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
        
        System.out.println("Transpose of the Matrix : ");
        for(int k = 0; k < 3; k++)
        {
            for(int l = 0; l < 3; l++)
            {
                System.out.print(a[l][k] + " ");
            }
            System.out.println();
        }
    }
}
