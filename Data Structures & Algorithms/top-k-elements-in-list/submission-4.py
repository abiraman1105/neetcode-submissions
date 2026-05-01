class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        hashmap = {}
        res = []
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for j in hashmap:
            bucket[hashmap[j]].append(j)

        for n in range(len(nums), -1, -1):
            while bucket[n]:
                res.append(bucket[n].pop())
                if len(res) == k:return res

        return res