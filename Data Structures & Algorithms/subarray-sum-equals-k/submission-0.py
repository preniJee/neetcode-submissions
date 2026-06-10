class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prf_sum = {0 : 1}
        curr_sum = 0
        cnt = 0
        # [2,-1,1, 2]
        for i,num in enumerate(nums):
            # update  the current sum
            curr_sum += num # = 2 , 1 , 2, 4
            # I wanna check if the difference has been seen before 
            diff = curr_sum - k # = 0 , 2- 1=1, 0 , 4 -2 = 2
            if diff in prf_sum: 
                cnt += prf_sum[diff] # cnt = 1, 2, 2 + 2 = 4
            prf_sum[curr_sum] = prf_sum.get(curr_sum,0) + 1 # prf_sum = {0:1, 2:2, 1:1, 4 :1 }
        return cnt

        
        
        
        