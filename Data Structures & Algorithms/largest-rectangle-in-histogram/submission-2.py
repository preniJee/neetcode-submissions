class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        
        left_extension = [0 for i in range(len(heights))] 
        right_extension = [0 for i in range(len(heights))]

        right_dir_stack = [(0,heights[0])]

        for i, height in enumerate(heights):
            while height < right_dir_stack[-1][1] :
                idx , h = right_dir_stack.pop()
                right_extension[idx] = i - idx 
                if not right_dir_stack :
                    break
            
            right_dir_stack.append((i,height))

        while right_dir_stack :
            idx , h = right_dir_stack.pop()
            right_extension[idx] = len(heights) - idx 


        left_dir_stack = [(len(heights)-1 , heights[-1])]

        for i in range(len(heights)-1, -1, -1) :
            height = heights[i]
        
            while height < left_dir_stack[-1][1] :
                idx , h = left_dir_stack.pop()
                left_extension[idx] =  - (i - idx)
                if not left_dir_stack :
                    break
                
            left_dir_stack.append((i,height))

        while left_dir_stack :
            idx , h = left_dir_stack.pop()
            left_extension[idx] = - (0 - idx) + 1


        max_area = 0
        for i in range(len(heights)) :
            width = left_extension[i] + right_extension[i] - 1
            area = width * heights[i]
            if area > max_area :
                max_area = area
        
        return max_area
