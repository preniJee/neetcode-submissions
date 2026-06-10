class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        answers = []
        n = len(nums)
        
        subset = []

        def backtrack(i):
            if i >= n:
                answers.append(subset.copy())
                return 
            # add nums[i] and backtrack i + 1
            subset.append(nums[i])
            backtrack(i+1)
            # dont add nums[i] and backtrack i +1
            subset.pop()
            backtrack(i+1)


        backtrack(0)
        return answers