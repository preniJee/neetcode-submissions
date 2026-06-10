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
        q.append(root)
        
        final_list = []

        while q :
            level_list = []
            q_len = len(q)
            for i in range(len(q)):
                curr_node =  q.popleft() 

                level_list.append(curr_node.val)

                if curr_node.left:
                    q.append(curr_node.left) # 
                if curr_node.right:
                    q.append(curr_node.right) # 

            if level_list:
                final_list.append(level_list)

        return final_list


    

            



        