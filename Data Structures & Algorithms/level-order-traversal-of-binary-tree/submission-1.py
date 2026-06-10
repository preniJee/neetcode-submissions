# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root):

        if not root:
            return []
        
      
        q = deque()
        q.append((root, 0))
        
        final_list = []

       
        curr_depth_list = []
        prev_depth = 0
        while q :
            print(q)
            curr_node, curr_depth = q.popleft() # node : 3  , curr_depth : 1
            
            if curr_node.left:
                q.append((curr_node.left, curr_depth + 1)) # 
            if curr_node.right:
                q.append((curr_node.right, curr_depth + 1)) # 
        
            if curr_depth == prev_depth : # (1, 1)
                curr_depth_list.append(curr_node.val) # [2,3]
            else : 
                final_list.append(curr_depth_list)  # [[1]]
                curr_depth_list = [curr_node.val] # [2]
                prev_depth = curr_depth  # prev = 1
                
        final_list.append(curr_depth_list)
        return final_list


    

            



        