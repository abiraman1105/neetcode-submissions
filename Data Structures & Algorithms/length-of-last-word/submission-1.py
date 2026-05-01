class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while r >= 0 and s[r] == " ":
            r -= 1
        length = 0
        while r >= 0 and s[r] != " ":
            length += 1
            r -= 1

        return length