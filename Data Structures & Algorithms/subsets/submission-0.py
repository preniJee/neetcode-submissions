class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        answers = []

        for num in nums:
            print(num, answers)
            num_subsets = [[num]]
            for subset in answers:
                # print(subset)
                num_subsets.append(subset + [num])
            
            answers.extend(num_subsets)
        
        answers.append([])

        return answers
        