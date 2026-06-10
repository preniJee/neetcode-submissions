class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining_first_idx = {}

        for i, num in enumerate(nums):
            remaining = target - num
            # print(remaining_first_idx)
            if  num in remaining_first_idx:
                return [remaining_first_idx[num] , i]
            else :
                remaining_first_idx[remaining] = i
            
    

        