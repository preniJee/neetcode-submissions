class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        stack.append(0)
        for i in range(1,len(temperatures)):
            t = temperatures[i]
            print(stack[-1])
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        # if stack : 
        #     for i in stack:
        #         result[i] = 0
        
        return result


        