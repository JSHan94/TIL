class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for i in set(nums):
            if nums.count(i) == 1 :
                return i
                
                
# class Solution(object):
#   def singleNumber(self, nums):
#       """
#       :type nums: List[int]
#       :rtype: int
#       """
#       a = 0
#       for i in nums:
#           a ^= i
#       return a
