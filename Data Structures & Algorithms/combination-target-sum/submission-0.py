class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        n = len(nums)
        answer = []
        combination = []
        #   nums=[2,5,6,9]
        #   target=9
        def backtrack(i) :
            if i >= n:
                if sum(combination) == target:
                    answer.append(combination.copy())
                return

            # one choice is not to add num[i]
            combs_sum = sum(combination) + nums[i] # 2
           
            # other choices are to add 1 time, 2 times , ... while the sum of comb=< target
            c = 0
            while combs_sum <= target:
                c += 1
                combination.append(nums[i])
                backtrack(i+1)
                combs_sum += nums[i]
            for j in range(c):
                combination.pop()
            backtrack(i+1)
            
                


        backtrack(0)
        return answer
