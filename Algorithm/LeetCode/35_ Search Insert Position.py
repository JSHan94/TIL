class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        mid = (start + end) //2
        
        while start < end:
            if nums[mid] < target :
                start = mid + 1 
            elif nums[mid] > target :
                end = mid 
            elif nums[mid] == target :
                return mid
            mid = (start+end)//2
        
        print(start,mid,end)
        if nums[mid] < target :
            return mid + 1
        else:
            return mid
