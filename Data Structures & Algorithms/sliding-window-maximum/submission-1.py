import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start_idx = 0
        end_idx = k

        max_list = list()
        while end_idx <= len(nums):
            curr_window = nums[start_idx : end_idx]
            window_heap = [-i for i in curr_window]
            heapq.heapify(window_heap)
            max_list.append(-(heapq.heappop(window_heap)))
            start_idx += 1
            end_idx += 1
        
        return max_list
        
