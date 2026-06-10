import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start_idx = 0
        end_idx =  k - 1  
        if len(nums) == 1:
            return nums
        curr_window = nums[start_idx : k]
        window_heap = [(-num,i) for i,num in enumerate(curr_window)]
        heapq.heapify(window_heap)
        max_list = [-(window_heap[0][0])]


        while end_idx < len(nums) - 1 :
            start_idx += 1
            end_idx += 1
            heapq.heappush(window_heap, (-nums[end_idx], end_idx))
            # pop until the max is in the window
            while window_heap[0][1] < start_idx :
                heapq.heappop(window_heap)

            max_list.append(-(window_heap[0][0]))

            
    
        return max_list
        
