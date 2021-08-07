class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s1 = 0 # can buy
        s2 = -prices[0] # can sell
        s3 = float('-inf')# after sell
        
        for i in prices:
            s2 = max(s1-i,s2)
            s1 = max(s1,s3)
            s3 = s2+i
            
        return max(s1,s3) 
