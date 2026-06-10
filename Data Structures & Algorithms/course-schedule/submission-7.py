class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        taken = set()

        prereq_dict = {c:[] for c in range(numCourses)}
        for c,req in prerequisites:
            prereq_dict[c].append(req)

        def dfs(c):
            if not prereq_dict[c]:
                return True
            if c in taken:
                return False
            taken.add(c)
            for req in prereq_dict[c]:
                if not dfs(req): return False
              
            prereq_dict[c] = 0
            # taken.remove(c)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True