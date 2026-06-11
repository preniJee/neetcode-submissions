# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = 0
        
        def dfs(node):
            
            if not node :
                return 0,0
            
            skip_left , rob_left = dfs(node.left)
            skip_right, rob_right = dfs(node.right)

            rob_cur = node.val + skip_left + skip_right
            skip_cur = max(rob_left, skip_left) + max(rob_right, skip_right)

            return skip_cur, rob_cur
        
        skip_root, rob_root = dfs(root)
        return max(skip_root, rob_root)
        

            


            
          
            



