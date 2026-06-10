class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1

        output = []

        for i,num in enumerate(nums) : 
            product = 1 
            for j, p in enumerate(nums):
                if j!=i: 
                    product *= p
            output.append(product)

        return output
        
