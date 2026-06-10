# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))







        # if  not root:
        #     return 0
        # q = deque()
        # q.append(root)

    
        # depth = 0
        
        # while q :
        #     q_len = len(q)
        #     for i in range(q_len):
        #         node = q.popleft()
        #         if node.left :
        #             q.append(node.left)
        #         if node.right : 
        #             q.append(node.right)
        #     depth += 1

        # return depth


        
        