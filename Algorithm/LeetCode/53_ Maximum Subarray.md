class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        maxium = total = nums[0]
        

        for n in nums[1:]:
                
            if total < 0 and n > total:
                total = n
            else:
                total += n
            
            maxium = max(maxium, total)
            
        return maxium
