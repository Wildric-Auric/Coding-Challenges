//Challenge: https://www.codewars.com/kata/5324945e2ece5e1f32000370/csharp

using System;
using System.Numerics;
public static class Kata
{
 public static string sumStrings(string a = "0", string b = "0")
    {
      if (a == "") {a = "0";}
      if (b == "") {b = "0";}
        BigInteger aa = BigInteger.Parse(a);
        BigInteger bb = BigInteger.Parse(b);
        int r = 0;
        int DecimalA = 0;
        int DecimalB = 0;
        int sum;
        int[] y = new int[0];
        int[] x = new int[0];
        int[] z;


        while ((aa != 0 || bb != 0))
        {

            if (aa != 0)
            {
                DecimalA = (int) (aa % 10);
                aa = aa /10;
            }
            else DecimalA = 0;
            if (bb != 0)
            {
                DecimalB = (int) (bb % 10);
                bb = bb / 10;
            }
            else DecimalB = 0;
            var temp = DecimalA + DecimalB + r;
            r = temp / 10;
            if ((aa == 0) && (bb == 0))
            {
               
                sum = temp;
            }
            else sum = temp % 10;


            x = new int[] { sum };
            z = y;
            y = new int[x.Length + z.Length];
            x.CopyTo(y, 0);
            z.CopyTo(y, x.Length);
        }
        string result = string.Join("", y);
            return result;
    }
}
