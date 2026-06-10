# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        def bfs(root):
            if not root :
                return []

            res = []
            q = deque([root])
            while q :
                level = []
                n = len(q)
                for i in range(n):
                    node = q.popleft()
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(level)
            return res
        
        res = bfs(root)
        print(res)
        right_side = []
        for level in res:
            right_side.append(level[-1])
        
        return right_side


        



        