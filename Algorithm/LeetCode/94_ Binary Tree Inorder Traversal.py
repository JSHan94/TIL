# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## iterative solution

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root 
        res = []
        while cur != None or len(stack) != 0 :
            while(cur != None):
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


## recursive solution

# class Solution:    
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if root == None:
#             return []
#         self.helper(root,res)
        
#         return res
    
#     def helper(self, node,res):
#         if node.left != None:
#             self.helper(node.left,res)
#         res.append(node.val)
#         if node.right != None:
#             self.helper(node.right,res)
        
