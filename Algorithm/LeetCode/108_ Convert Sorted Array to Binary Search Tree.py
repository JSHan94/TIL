class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
        def convert(left,right):
            if left > right  :
                return None
            
            mid = (left + right) //2
            root = TreeNode()    
            root.val = nums[mid]
            root.left = convert(left,mid-1)
            root.right = convert(mid+1,right)
            return root
        return convert(0,len(nums)-1)
