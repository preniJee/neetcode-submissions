class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_idx = 0
        n = len(nums)
        
        for i in range(n):
            if max_idx >= i:
                max_idx = max(max_idx, i + nums[i])

        if max_idx < n -1 :
            return False
        else:
            return True
         