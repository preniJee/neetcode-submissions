class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1] * len(nums)
       
        prefix_product = 1
        for i in range(len(nums)-1):
            prefix_product *= nums[i]
            prefix.append(prefix_product)

    
        suffix_product = 1
        for i in range(len(nums) -1 , 0 , -1):
            suffix_product *= nums[i]
            suffix[i-1] = suffix_product
            print(i)
            print(suffix)

        print(prefix)
        print(suffix)
        output = []
        for i in range(len(nums)):
            output.append(prefix[i]*suffix[i])
        
        return output
        

        
