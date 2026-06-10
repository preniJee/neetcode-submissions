class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        length = 0
        for num in nums:
            if num-1 not in hash_set:
                curr_num = num
                curr_len = 1

                while curr_num +1 in hash_set :
                    curr_num += 1
                    curr_len += 1
            
                length = max(length, curr_len)
        
        return length


        