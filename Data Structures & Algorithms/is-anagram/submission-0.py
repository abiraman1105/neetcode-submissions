class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        count_s = {}
        count_t = {}
        for i in s:
            count_s[i] = 1 + count_s.get(i, 0)
        for i in t:
            count_t[i] = 1 + count_t.get(i, 0)
        
        for j in count_s:
            if j not in count_t or count_s[j] != count_t[j]:  
                return False
            # elif count_s[j] != count_t[j]: return False
        
        return True