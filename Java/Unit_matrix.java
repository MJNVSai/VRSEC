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
public class Unit_matrix 
{
    public static void main(String args[])
    {
        int i,j;
        int a[][] = new int[3][3];
        
        for(i = 0; i < 3; i++)
        {
            for(j = 0; j < 3; j++)
            {
                if(i == j)
                {
                    a[i][j] = 1;
                }
                else
                {
                    a[i][j] = 0;
                }
            }
        }
        
        System.out.println("Unit Matrix : ");
        for(int k = 0; k < 3; k++)
        {
            for(int l = 0; l < 3; l++)
            {
                System.out.print(a[k][l] + " ");
            }
            System.out.println();
        }
    }
}
