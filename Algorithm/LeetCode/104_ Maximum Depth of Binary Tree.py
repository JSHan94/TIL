# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None :
            return 0
        return self.travel(root,1)
        
    def travel(self,node,depth):
        ld = rd = depth
        if node.left != None :
            ld = self.travel(node.left,depth+1)
        if node.right != None:
            rd = self.travel(node.right,depth+1)
        return max(ld,rd)
