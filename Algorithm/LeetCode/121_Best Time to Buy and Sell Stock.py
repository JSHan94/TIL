class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = 9999999
        maxP = 0
        for i in prices:
            if i < minP :
                minP = i
            if i - minP > maxP:
                maxP = i-minP
        
        return maxP
