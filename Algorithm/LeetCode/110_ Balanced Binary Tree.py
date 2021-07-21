class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if node == None :
                return 0
            
            left = height(node.left)
            right = height(node.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1 :
                return -1
            
            return 1+ max(left,right)
        
        return height(root) != -1
