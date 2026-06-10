class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l , r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        pivot = l

        def binary_search(left,right,target):

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    left = mid+1
                else :
                    right = mid - 1
            return -1
            
        result = binary_search(0, pivot-1, target)
        if result != -1 :
            return result
        return binary_search(pivot, len(nums)-1, target)





        

