class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        prefix_sum = [nums[0]] * n

        for i in range(1, n): 
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        # DP [i] the max sum up to i-th point in nums
        DP = [0] * n
        DP[0] = nums[0]
        for i in range(1 , n):
            if DP[i-1] >=0  :
                DP[i] = DP[i-1] + nums[i]
            else : 
                DP[i] = nums[i]




        return max(DP)
        