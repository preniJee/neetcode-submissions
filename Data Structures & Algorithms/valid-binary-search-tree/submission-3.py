# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
   
    def check_dfs(self, root, root_range):
        if not root_range[0] < root.val < root_range[1]:
            return False
        if root.left:
            left_range = (root_range[0], root.val)
            left_valid =  self.check_dfs(root.left, left_range)
            if not left_valid :
                return False
        if root.right:
            right_range = (root.val, root_range[1])
            right_valid = self.check_dfs(root.right, right_range)
            if not right_valid :
                return False
       
        return True
        
  
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check_dfs(root, (float("-inf"), float("+inf")))
        
      
      
        
            

                
            
        
        

        