
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s)!=set(t) :
            return False

        s_dict = {}
        t_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] +=1
            else :
                s_dict[char] = 1
        
        for char in t:
            if char in t_dict:
                t_dict[char] +=1
            else :
                t_dict[char] = 1
        
        for key in s_dict:
            if s_dict[key]!=t_dict[key]:
                return False
        return True

        