class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq_dict = {c:[] for c in range(numCourses)}
        for c,req in prerequisites:
            prereq_dict[c].append(req)

        output = []
        valid_order = set()
        taken = set() # been visited and added to output
        cycle = set()
        # detect a cycle but also update the valid order
        def dfs(c):
            if c in cycle:
                return False
            if c in valid_order: 
                return True

            cycle.add(c)

            for req in prereq_dict[c]:
                if not dfs(req): return False
            
            
            cycle.remove(c)
            valid_order.add(c)
            output.append(c)
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
            
        
        return output