import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        heapq.heapify(self.heap)
        for i in range(len(nums)):
            if i < k :
                heapq.heappush(self.heap,nums[i])
                continue
            heapq.heappushpop(self.heap,nums[i])
        

    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        print(val, self.heap, self.heap[0])
        return self.heap[0] 
    
        
