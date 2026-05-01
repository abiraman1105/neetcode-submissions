class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        curr = set()
        l, r = 0, 0

        while r < len(s):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])

            res = max(res, r - l + 1)
            r += 1

            


        return res
