class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root == None :
            return res
        
        self.postT(root,res)
        return res
        
    def postT(self, node,res):
        if node.left != None :
            self.postT(node.left,res)
        if node.right != None:
            self.postT(node.right,res)
        res.append(node.val)
