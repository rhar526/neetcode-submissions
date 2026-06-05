class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            prod = 1
            for j, n in enumerate(nums):
                if i == j:
                    prod *= 1
                else:
                    prod*=n
            res.append(prod)
        return res