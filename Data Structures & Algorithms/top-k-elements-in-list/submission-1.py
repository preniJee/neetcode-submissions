import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_num_list = {i+1 : [] for i in range(len(nums))}

        num_count = {}
        for i,num in enumerate(nums): # O(n)
            if num in num_count: 
                num_count[num] += 1
            else : num_count[num] = 1
        for num,count in num_count.items(): # O(n)
            freq_num_list[count].append(num)
        
        final_nums = []
        for freq in range(len(nums), 0, -1) :
            if len(final_nums) < k :
                final_nums.extend(freq_num_list[freq])
            
        return final_nums



        
            