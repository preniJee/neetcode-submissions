# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0

        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)

            curr_d = left_height + right_height
            self.max_d  = max(self.max_d , curr_d)
            return max(left_height, right_height) + 1
        
        root_height = height(root)
        return self.max_d


     


        
        