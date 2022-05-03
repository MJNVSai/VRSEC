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
public class Totalarmstrong 
{
    public static void main(String args[])
    {
        System.out.println();
        
        int num, count = 1, rem, sum;
        
        while(count < 500)
        {
            num = count;
            sum = 0;
            
            while(num != 0)
            {
                rem = num%10;
                sum = sum + (rem*rem*rem);
                num = num/10;
            }
            if(count == sum)
            {
                System.out.println(sum + " is an Armstrong number ");
            }
            count = count + 1;
        }
    }
}
