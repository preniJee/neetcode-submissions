# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0 
        return 1 + max(self.height(root.left),self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            dfs_left = dfs(root.left)
            dfs_right = dfs(root.right)

            balanced = dfs_left[0] and dfs_right[0] and abs(dfs_left[1] - dfs_right[1]) <= 1

            return [balanced, 1 + max(dfs_left[1],dfs_right[1])]
        
        return dfs(root)[0]

        # if not root :
        #     return True
        # if abs(self.height(root.left) - self.height(root.right)) > 1 :
        #     return False
        # else :
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)


        