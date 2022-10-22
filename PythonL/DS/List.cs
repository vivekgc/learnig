using System;
using System.Collections.Generic;
using System.Linq;
class Demo {
   static void Main() {
      List<long> list = new List<long> { 150, 300, 400, 350, 450, 550, 600 };
      foreach(long ele in list){
         Console.WriteLine(ele);
      }

      // getting largest element
      long max_num = list.AsQueryable().Max();

      // getting smallest element
      long min_num = list.AsQueryable().Min();

      Console.WriteLine("Smallest number = {0}", min_num);
      Console.WriteLine("Largest number = {0}", max_num);
   }
}