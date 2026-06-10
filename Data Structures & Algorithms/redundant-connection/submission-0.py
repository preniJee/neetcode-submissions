class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)


        def has_cycle(node, par):
            if node in visited : 
                return True
            visited.append(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if has_cycle(nei, node): 
                    return True
            return False
                
                
            

        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = []

            if has_cycle(u, -1):
                return [u,v]
        return []



        