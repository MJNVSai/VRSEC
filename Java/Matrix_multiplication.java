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
public class Matrix_multiplication 
{
   public static void main(String args[])
    {
        int i,j,row,col,row1,col1;
        int a[][] = new int[3][3];
        int b[][] = new int[3][3];
        int c[][] = new int[3][3];
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter No.of Rows for Matrix 1: ");
        row = sc.nextInt();
        System.out.print("Enter No.of Columns for Matrix 1: ");
        col = sc.nextInt();
        System.out.print("Enter No.of Rows for Matrix 2: ");
        row1 = sc.nextInt();
        System.out.print("Enter No.of Columns for Matrix 2: ");
        col1 = sc.nextInt();
        
        if(col == row1)
        {
            System.out.println("Enter Matrix 1 elements : ");
            for(i = 0; i < row; i++)
            {
                for(j = 0; j < col; j++)
                {
                    a[i][j] = sc.nextInt();
                }
                System.out.println();
            }
            
            System.out.println("Enter Matrix 2 elements : ");
            for(int i1 = 0; i1 < row1; i1++)
            {
                for(int j1 = 0; j1 < col1; j1++)
                {
                    b[i1][j1] = sc.nextInt();
                } 
                System.out.println();
            }
            
             for(int k = 0; k < row; k++)
             {
                 for(int k1 = 0; k1 < col1; k1++)
                 {
                     c[k][k1] = 0;
                     for(int l = 0; l < row1; l++)
                     {
                         c[k][k1] = c[k][k1] + (a[k][l]*b[l][k1]);
                     }
                 }
             }
             System.out.println();
             System.out.println("Matrix Multiplictaion : ");
             for(int x = 0; x < row; x++)
             {
                 for(int y = 0; y < col1; y++)
                 {
                     System.out.print(c[x][y] + " ");
                 }
                 System.out.println();
             }
        }
        else
        {
            System.out.println("Multiplication Can't be performed");
        }
        
    } 
}
