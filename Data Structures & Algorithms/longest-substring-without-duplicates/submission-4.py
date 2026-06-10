class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0 
        max_len = 0
        sub = {}
        for r in range(len(s)):
            if not s[r] in sub:
                sub[s[r]] = r
            else: 
                l = max(sub[s[r]] + 1, l)
                sub[s[r]] = r
            max_len = max(max_len,r-l+1)
        
        return max_len


            
        