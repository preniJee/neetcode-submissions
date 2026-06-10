# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # edge cases when one is child of the other 

        q_ans = []
        p_and = []
        ans_memory = {root.val : [(root,0)]}
        # update each nodes ancestors in bfs search
        def dfs(node,level):
            # if not node:
            #     return
            if p.val in ans_memory and q.val in ans_memory:
                return 
            if node.left:
                if not node.left.val in ans_memory:
                    ans_memory[node.left.val] = [(node.left, level+1)]
                ans_memory[node.left.val].extend(ans_memory[node.val])
                # print(f"curr: {node.val}, left : {node.left.val} : {ans_memory[node.left]}", )
                dfs(node.left, level + 1)
            
            if node.right: 
                if not node.right.val in ans_memory:
                    ans_memory[node.right.val] = [(node.right, level+1)]
                ans_memory[node.right.val].extend(ans_memory[node.val])
                # print(f"curr: {node.val}, right : {node.right.val} : {ans_memory[node.right]}", )
            
                dfs(node.right, level + 1)  



        dfs(root,0)
        LCA = (None, 0)
      
        for p_ans in ans_memory[p.val]:
            for q_ans in ans_memory[q.val]:
                if p_ans[0] == q_ans[0]:
                    if p_ans[1] >= LCA[1]:
                        LCA = p_ans
        return LCA[0]




        