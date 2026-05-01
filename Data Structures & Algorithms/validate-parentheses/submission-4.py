class Solution:
    def isValid(self, s: str) -> bool:
        hash_map={
            ']':'[',
            ')':'(',
            '}':'{'
        }
        stack =[]
        for i in s:
            if i not in hash_map:
                stack.append(i)
            else:
                if not stack or stack.pop() != hash_map[i]:return False
                
        return stack == []
