class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f = [0 for i in range(n)]
        
        f[0], f[1] = cost[0], cost[1]
        
        for i in range(2,n):
            f[i]=cost[i] + min(f[i-1],f[i-2])
        
        return min(f[-1],f[-2])