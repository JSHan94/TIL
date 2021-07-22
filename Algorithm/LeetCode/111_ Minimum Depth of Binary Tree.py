# 가장 먼저 자식이 없는 경우 == min depth
# bfs로 depth 단위로 노드를 읽음

class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        def bfs(root):
            queue = []
            queue.append(root)
            depth = 1
            while queue != [] :
                for i in range(len(queue)):
                    node = queue.pop(0)
                    if not node.left and not node.right:
                        return depth
                    if node.left :
                        queue.append(node.left)
                    if node.right :
                        queue.append(node.right)
                depth +=1
                
        
        return bfs(root)
