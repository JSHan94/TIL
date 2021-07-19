class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None :
            return res
        
        self.preT(root,res)
        return res
        
    def preT(self, node,res):
        
        res.append(node.val)
        if node.left != None :
            self.preT(node.left,res)
        if node.right != None:
            self.preT(node.right,res)
