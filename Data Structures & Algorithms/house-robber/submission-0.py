class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]

        DP = [0] * n
        DP[0] = nums[0]
        DP[1]= max(nums[1], DP[0])

        for i in range(2,n):
            DP[i] = max(DP[i-1], DP[i-2] + nums[i])

        return DP[n-1]
        