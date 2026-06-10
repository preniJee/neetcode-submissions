class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first_index = 0
        # second_index = 0
        needed_numbers = []
        for i in nums:
            needed_numbers.append(target-i)
        
        print(nums)
        print(needed_numbers)
        for i, num in enumerate(needed_numbers):
            if num in nums :
                first_index = i
                second_index = nums.index(num)
                print(first_index)
                print(second_index)
                
        
        return [min(first_index,second_index), max(first_index,second_index)]

