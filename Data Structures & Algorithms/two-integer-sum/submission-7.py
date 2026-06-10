class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_index = 0
        second_index = 0
        needed_numbers = []
        for i in nums:
            needed_numbers.append(target-i)
        
        for i, num in enumerate(needed_numbers):
            if (num in nums) and (nums.index(num)!=i):
                first_index = i
                second_index = nums.index(num)
                break
        
        return [min(first_index,second_index),max(first_index,second_index)]

