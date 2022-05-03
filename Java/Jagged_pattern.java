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
public class Jagged_pattern 
{
    public static void main(String args[])
    {
        int a[][] = new int[4][];
        a[0] = new int[1];
        a[1] = new int[2];
        a[2] = new int[3];
        a[3] = new int[4];
        
        int x = 1,i,j,i1,j1;
        for(i = 0; i < a.length; i++)
        {
            for(j = 0; j < a[i].length; j++)
            {
                a[i][j] = x++;
            }
        }
        System.out.println("Jagged pattren : ");
        for(i1 = 0; i1 < a.length; i1++)
        {
            for(j1 = 0; j1 < a[i1].length; j1++)
            {
                System.out.print(a[i1][j1] + " ");
            }
            System.out.println();
        }
    }
}
