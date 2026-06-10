class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        if len(s) == 1:
            return 1

        start_idx = 0
        sub_str_len = 0 
        max_len = 0
        sub_str_idx = {}

        for i in range(len(s)):
            print(sub_str_idx)
            if s[i] not in sub_str_idx:
                sub_str_idx[s[i]] = i
            else :
                dup_idx = sub_str_idx[s[i]]
                start_idx = dup_idx + 1
                # check the max len and then update the substring
                max_len = max(max_len, len(sub_str_idx))
                sub_str_idx = {}
                for idx in range(start_idx, i+1):
                    sub_str_idx[s[idx]] = idx
            max_len = max(max_len, len(sub_str_idx))
            

        
        return max_len  
            
        
               
            




        