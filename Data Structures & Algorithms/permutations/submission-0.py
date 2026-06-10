class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = [False] * len(nums)

        answers = []

        perm = []

        def backtrack(perm, visited):
            if len(perm) == len(nums):
                answers.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not visited[i]:
                    perm.append(nums[i])
                    visited[i] = True
                    backtrack(perm, visited)

                    visited[i] = False
                    perm.pop()
                  

        for i in range(len(nums)):
            visited[i] = True
            perm.append(nums[i])
            backtrack(perm, visited)
            visited[i] = False
            perm = []



        return answers
