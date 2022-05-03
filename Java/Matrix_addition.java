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
public class Matrix_addition 
{
    public static void main(String args[])
    {
        int i,j;
        int a[][] = new int[3][3];
        int b[][] = new int[3][3];
        int c[][] = new int[3][3];
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
        
        System.out.println("Enter Matrix 2 elements : ");
        for(int i1 = 0; i1 < 3; i1++)
        {
            for(int j1 = 0; j1 < 3; j1++)
            {
                b[i1][j1] = sc.nextInt();
            } 
            System.out.println();
        }
        
        for(int k = 0; k < 3; k++)
        {
            for(int l = 0; l < 3; l++)
            {
                c[k][l] = a[k][l] + b[k][l];
            } 
        }
        
        System.out.println("Addition of Matrixes : ");
        for(int k1 = 0; k1 < 3; k1++)
        {
            for(int l1 = 0; l1 < 3; l1++)
            {
                System.out.print(c[k1][l1] + " ");
            }
            System.out.println();
        }
    }
}
