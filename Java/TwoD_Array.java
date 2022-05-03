/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package pkg208w1a12a0;
import java.io.*;
/**
 *
 * @author SHREE
 */
public class TwoD_Array 
{
    public static void main(String args[])
    {
        int i,j;
        int a[][] =  {{10,20},{30,40}};
        
        System.out.println("2D Array Elements : ");
        for(i =0; i < 2; i++)
        {
            for(j = 0; j < 2; j++)
            {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
    }
}
