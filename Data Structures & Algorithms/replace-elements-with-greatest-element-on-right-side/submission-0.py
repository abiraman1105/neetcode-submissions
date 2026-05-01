class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new = []
        for i in range(len(arr)):
            m = -1
            for j in range(i + 1,len(arr)):
                m = max(m, arr[j])
            new.append(m)
        return new

