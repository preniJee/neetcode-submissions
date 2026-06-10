class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        if len(edges) < n-1:
            return False

        adj_dict = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj_dict[n1].append(n2)
            adj_dict[n2].append(n1)
        
        cycle_path = set() # once see the node in the path add to this
        # detect cycle starting from one node
        def dfs(node, next_node):
            if node in cycle_path:
                return False
            cycle_path.add(node)
           
            for nei in adj_dict[node]:
                if nei == next_node:
                    continue
                if not dfs(nei, node) : 
                    return False
        
            return True
            
        return dfs(0,-1) and len(cycle_path) == n