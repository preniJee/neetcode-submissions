class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        if len(s) == 1:
            return 1

        left = 0

        max_len = 0
        sub = set()

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[left])
                left +=1
            sub.add(s[r])
            max_len = max(max_len, r - left + 1)
        return max_len
        




           

        
        return max_len  
            
        
               
            




        