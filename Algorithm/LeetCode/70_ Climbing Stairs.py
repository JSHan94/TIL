
# O(n^2) ? 
class Solution:
    def fac(self,n):
        res = 1
        for i in range(1,(n+1)):
            res *= i
        return res
    
    def climbStairs(self, n: int) -> int:
        max_two = n//2
        res = 0 
        for two_num in range(max_two+1):
            one_num = n - 2*two_num
            res += self.fac(one_num+two_num) // (self.fac(one_num) * self.fac(two_num))
            #print(res)
        return res
      
 

# This answer will be Fibonacci, So there log(n) solution

# public class Solution {
#     public int climbStairs(int n) {
#         double sqrt5=Math.sqrt(5);
#         double fibn=Math.pow((1+sqrt5)/2,n+1)-Math.pow((1-sqrt5)/2,n+1);
#         return (int)(fibn/sqrt5);
#     }
# }
