class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        count = defaultdict(int)
        ans = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l +1)
        
        return ans




        # l = 0
        # r = 0 
        # max_len = 0
        # sub = {}
        # for r in range(len(s)):
        #     if not s[r] in sub:
        #         sub[s[r]] = r
        #     else: 
        #         l = max(sub[s[r]] + 1, l)
        #         sub[s[r]] = r
        #     max_len = max(max_len,r-l+1)
        
        # return max_len


            
        