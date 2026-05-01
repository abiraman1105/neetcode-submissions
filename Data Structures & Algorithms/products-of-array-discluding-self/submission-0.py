class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = []
        postfix = [0] * len(nums)

        for i in nums:
            product = product * i
            prefix.append(product)

        product = 1

        for i in range(len(nums) - 1 , -1, -1):
            product = product * nums[i]
            postfix[i] = product

        res = []
        for i in range(len(nums)):
            pre = 1 if i - 1 < 0 else prefix[i - 1]
            post = 1 if i + 1 == len(nums) else postfix[i + 1]
            
            res.append(pre * post)

        return res
