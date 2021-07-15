class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None :
            return True
        if p == None or q == None :
            return False
        if p.val != q.val :
            return False
        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) :
            return True
        
