class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left_p = 0
        right_p = len(heights) - 1

        while left_p != right_p :
            width = right_p - left_p
            height = min(heights[right_p], heights[left_p])
            area = width * height
            if area > max_area:
                max_area = area
            if heights[right_p] < heights[left_p] :
                right_p -= 1
            else :
                left_p += 1
        
        return max_area
            

            
        