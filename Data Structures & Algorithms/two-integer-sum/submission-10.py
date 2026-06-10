class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}

        for i,num in enumerate(nums):
            if num in needed:
                print(needed[num])
                # ans = sorted([num, nums[needed[num]]])
                return [needed[num], i]
            else:
                # for num + x to be target we need x , or target - num

                needed[target-num] = i

        

        