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
public class Matrix_equal 
{
    public static void main(String args[])
    {
        int i,j,count = 0;
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
                if(a[k][l] == b[k][l])
                {
                    count = count + 1;
                }
            }
        }
        if(count == 9)
        {
            System.out.println("Matrix's are Equal ");
        }
        else
        {
            System.out.println("Matrix's are not Equal");
        }
    }
}
