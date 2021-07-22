# 자기 노드 까지의 sum을 알기 위해 stack에 넣을때 tuple로 삽입 

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root :
            return False
        res = 0
        stack = [(root,0)]
        while stack :
            node, s  = stack.pop()
            s += node.val
            if not node.left and not node.right:
                if s == targetSum:
                    return True
            if node.left:
                stack.append((node.left,s))
            if node.right :
                stack.append((node.right,s))
        return False
